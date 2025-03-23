# 1. N(<= 16)명의 선수 후보들 중 K(<= N)명 선택해서 출전
# 2. A[i][j] = i와 j가 동시에 팀에 속할 때, i의 능력치의 증가/감소
# 3. 팀의 최대 능력치 출력


from itertools import combinations

filename = 'input9.txt'  # 파일 읽기
f = open(filename, 'r')
lines = f.readlines()

ability_list = []

for i in range(len(lines)):
    if i == 0:
        N = int(lines[i].rstrip())  # N: 선수 후보 인원수
    elif i == N+1:
        k = int(lines[i].rstrip())  # k: 출전 팀 인원수
    else:
        ability_list.append(list(map(int, lines[i].rstrip().split())))  # ability: N x N 능력치 배열

comb = list(combinations(list(range(0, N)), k))
max_ability = -999999999

for c in comb:  # 가능한 모둔 조합 탐색
    ability_sum = 0  # 능력치는 0으로 초기화
    for a in c:  # 조합에 속한 선수들의 능력치 계산
        for b in c:
            ability_sum += ability_list[a][b]
    max_ability = max(max_ability, ability_sum)  # 최대 능력치로 갱신

print(max_ability)  # 팀의 최대 능력치 출력
