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

print(dp[N-1][W])  # N-1번째 아이템을 확인했을 때(최대 가격)의 값 출력
