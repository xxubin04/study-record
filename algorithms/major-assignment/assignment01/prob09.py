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

for c in comb:
    ability_sum = 0
    for a in c:
        for b in c:
            ability_sum += ability_list[a][b]
    max_ability = max(max_ability, ability_sum)

print(max_ability)

# TC 1
# 4
# 2 3 1 5
# 1 4 -2 2
# 0 -1 3 5
# 2 4 2 1
# 3

# TC 2 -> 0
# 4
# 1 -4 -2 -5
# 0 2 -3 -2
# -2 -3 4 -2
# -1 -3 -4 6
# 3

# TC 3
# 8
# 6 -2 8 -5 3 6 0 -2
# 8 4 -12 8 3 6 -18 23
# -8 7 2 16 4 -8 -2 7
# 6 4 1 9 8 2 9 3
# -2 8 3 6 4 -2 -8 6
# 3 -2 4 7 2 8 9 12
# 2 8 3 -6 4 -2 8 6
# -4 3 2 9 4 6 9 8
# 5

# TC 4
# 10
# 2 -3 4 8 6 -2 9 -3 4 6
# -9 2 3 4 2 4 -2 3 -9 7
# 4 -2 7 3 4 7 -2 -9 3 -4
# 7 2 9 3 8 7 4 8 9 2
# 2 -3 -8 7 4 6 -2 8 7 4
# -6 1 2 9 8 4 9 1 2 8
# 4 7 9 -4 2 -3 9 4 7 2
# 3 9 4 7 2 9 8 3 4 -7
# 9 2 8 3 7 -4 9 2 3 7
# 2 3 -8 9 4 9 8 2 7 3
# 6