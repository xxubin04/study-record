import json
import pandas as pd
import os
from glob import glob  # 파일 이름 패턴으로 리스트를 가져오는 모듈

# 파일 읽어옴
with open("/content/drive/MyDrive/데이터사이언스 실습/csse_covid_19_data/country_convert.json", 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

# 나라 이름 변경 함수
def country_name_convert(row):
    if row['Country_Region'] in json_data:  # 각 행의 Country_Region 값이 json_data에 존재하면 표준 국가명으로 변경
        return json_data[row['Country_Region']]
    return row['Country_Region']

# 사망자/회복자 데이터 전처리 함수
def create_dataframe(filename):
    doc = pd.read_csv(filename, encoding='utf-8-sig')  # csv 파일을 dataframe으로 읽어오기

    data_dict = {}  # 사망자/회복자 컬럼에 해당하는 데이터를 각각 저장하는 딕셔너리

    # 사망자 컬럼 추출
    try:
        data_dict['Deaths'] = doc[['Country_Region', 'Deaths']]  # Deaths 컬럼만 dataframe으로 만들기
    except:
        data_dict['Deaths'] = doc[['Country/Region', 'Deaths']]
        data_dict['Deaths'].columns = ['Country_Region', 'Deaths']

    # 회복자 컬럼 추출
    try:
        data_dict['Recovered'] = doc[['Country_Region', 'Recovered']]  # Recovered 컬럼만 dataframe으로 만들기
    except:
        data_dict['Recovered'] = doc[['Country/Region', 'Recovered']]
        data_dict['Recovered'].columns = ['Country_Region', 'Recovered']

    data_processed_list = []  # 전처리된 데이터 저장하는 리스트

    # Deaths와 Recovered 컬럼에 대해 각각 dataframe 만들기
    for col in (columns_list := ["Deaths", "Recovered"]):
        try:
            df = doc[['Country_Region', col]]
        except:
            df = doc[['Country/Region', col]]
            df.columns = ['Country_Region', col]

        # 각각의 컬럼에 없는 데이터(NaN, 결측치) 삭제
        data_dict[col] = data_dict[col].dropna(subset=[col])
        doc['Country_Region'] = data_dict[col].apply(country_name_convert, axis=1)  # 'Country_Region'의 국가명을 표준 국가명으로 변경
        data_dict[col] = data_dict[col].astype({col: 'int64'})    # 각각의 컬럼의 데이터 타입을 숫자형으로 변경
        data_dict[col] = data_dict[col].groupby('Country_Region').sum()  # 같은 국가에 대한 데이터 합치기

        # 파일명을 기반으로 날짜 문자열을 반환하고, 컬럼명 변경
        date_column = filename.split('/')[-1].split('.')[0].lstrip('0').replace('-', '/')
        data_dict[col].columns = [date_column]

    # 전처리된 사망자/회복자 dataframe을 담은 딕셔너리 반환
    return data_dict

def generate_dataframe_by_path():

    PATH = "/content/drive/MyDrive/데이터사이언스 실습/COVID-19-master/csse_covid_19_daily_reports/"
    csv_list = list()

    file_list = sorted(glob(PATH + '*.csv'))  # 폴더 내의 모든 csv 파일 목록을 불러오고 정렬함

    # 사망자/회복자 데이터를 누적해서 저장할 빈 dataframe을 각각 생성함
    deaths_total = pd.DataFrame()
    recovered_total = pd.DataFrame()

    # file_list에 저장된 각 csv 파일에 대해 반복 처리
    for file in file_list:
        try:
            data = create_dataframe(file)  # csv파일 전처리 함수를 사용하여 전처리

            # 사망자 데이터를 기존 dataframe과 합치기
            deaths_total = pd.merge(deaths_total, data['Deaths'], how='outer', left_index=True, right_index=True)

            # 회복자 데이터를 기존 dataframe과 합치기
            recovered_total = pd.merge(recovered_total, data['Recovered'], how='outer', left_index=True, right_index=True)

        except Exception as e:  # 에러가 나는 파일은 건너뜀
            continue

    # 합쳐진 사망자/회복자 데이터를 csv 파일로 저장
    deaths_total.to_csv("final_df_deaths.csv", encoding='utf-8-sig')
    recovered_total.to_csv("final_df_recovered.csv", encoding='utf-8-sig')

    # 두 개의 최종 dataframe을 반환
    return deaths_total, recovered_total

# 사망자/회복자 데이터를 전처리하여 final_deaths, final_recovered로 저장
final_deaths, final_recovered = generate_dataframe_by_path()
