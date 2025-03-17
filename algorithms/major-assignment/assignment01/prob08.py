# 1. 배낭 문제
# 2. 배낭에 담긴 아이템들의 무게 총량 <= W && 가격의 최대


filename = 'input.txt'  # 파일 읽기
f = open(filename, 'r')
lines = f.readlines()

for i in range(len(lines)):
    if i == 0:
        N = int(lines[i].rstrip())  # N: 아이템의 개수
    elif i == 1:
        W = int(lines[i].rstrip())  # W: 배낭의 용량
    elif i == 2:
        w_list = list(map(int, lines[i].rstrip().split()))  # w_list: 아이템의 무게 리스트
    else:
        v_list = list(map(int, lines[i].rstrip().split()))  # v_list: 아이템의 가격 리스트

dp = [[0] * (W+1) for _ in range(N)]

for i in range(N):  # 아이템
    for j in range(W+1):  # 무게
        if j < w_list[i]:  # 배낭에 담을 수 있는 무게 j보다 아이템의 무게가 큰 경우
            dp[i][j] = dp[i-1][j]  # 배낭에 해당 아이템을 담지 않음
        else:  # 배낭에 담을 수 있는 무게 j보다 아이템의 무게가 작거나 같은 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_list[i]] + v_list[i])
            # 배낭에 담지 않는 경우와 배낭에 담는 경우에서의 가격 중 더 큰 경우를 선택함
            # i번째 아이템을 담는다면, 해당 아이템의 무게를 뺀 배낭의 용량에서 구할 수 있는 최대 가격에
            # 해당 아이템의 가격을 더함

print(dp[N-1][W])  # N-1번째 아이템을 W 용량에 담았을 때의 값 출력

# TC 1
# 6
# 30
# 5 10 8 6 9 3
# 20 40 30 25 35 15

# TC 2
# 10
# 45
# 2 6 12 8 15 10 9 11 4 7
# 10 25 35 20 45 30 28 33 15 23

# TC 3
# 15
# 60
# 4 12 8 5 10 14 7 11 6 9 15 3 13 2 1
# 15 35 25 20 30 40 22 33 18 28 45 10 38 8 5

# TC 4
# 12
# 40
# 6 8 5 11 3 10 9 7 12 4 13 2
# 25 30 20 35 15 33 28 22 40 18 38 10