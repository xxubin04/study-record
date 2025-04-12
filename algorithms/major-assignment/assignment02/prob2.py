# 사람 객체
class Person:
    def __init__(self, name, company, address, zipcode, phones, email):
        self.name = name
        self.company = company
        self.address = address
        self.zipcode = zipcode
        self.phones = phones
        self.email = email

    def print_person_info(self):  # 사람의 정보 출력
        print(f"{self.name}")
        print(f"     Company: {self.company}")
        print(f"     Address: {self.address}")
        print(f"     Zipcode: {self.zipcode}")
        print(f"     Phones: {self.phones}")
        print(f"     Email: {self.email}")

while True:
    print('$', end=' ')
    cmd = input().rstrip().split()  # 명령 입력받기
    if cmd[0] == "read":  # 파일 읽기
        address_book = []
        with open(cmd[1], 'r') as f:  # 입력받은 파일 열기
            lines = f.readlines()  # 파일에 저장된 각각의 라인을 리스트 형태로 저장

            for line in lines:
                info = line.split(' | ')  # | 를 기준으로 문자열 나누기
                # 사람을 객체로 저장
                address_book.append(Person(info[0].strip(), info[1].strip(),
                                           info[2].strip(), info[3].strip(),
                                           info[4].strip(), info[5].strip()))
    elif cmd[0] == "sort":  # 정렬
        if cmd[1] == "-name":  # 이름 기준
            address_book.sort(key=lambda x: x.name)
        elif cmd[1] == "-company":  # 회사 기준
            address_book.sort(key=lambda x: x.company)
        elif cmd[1] == "-address":  # 주소 기준
            address_book.sort(key=lambda x: x.address)
        elif cmd[1] == "-zipcode":  # 우편번호 기준
            address_book.sort(key=lambda x: x.zipcode)
        elif cmd[1] == "-phones":  # 전화번호 기준
            address_book.sort(key=lambda x: x.phones)
        elif cmd[1] == "-email":  # 이메일 주소 기준
            address_book.sort(key=lambda x: x.email)
    elif cmd[0] == "print":  # 출력
        for i in range(len(address_book)):
            address_book[i].print_person_info()
    elif cmd[0] == "exit":  # 그만두기
        break