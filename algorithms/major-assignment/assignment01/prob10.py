filename = 'input10.txt'
f = open(filename, 'r')
lines = f.readlines()
info = []

for i in range(len(lines)):
    if i == 0:
        N = int(lines[i].rstrip())  # N: 물건의 개수
    elif i == N+1:
        W = int(lines[i].rstrip())  # W: 최대 부피의 총량
    else:  # 물건당 (부피, 가격, 폐기비용) 입력받음
        info.append(list(map(int, lines[i].rstrip().split())))

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):  # 물건들 순차적으로 확인
    for j in range(W+1):  # 부피별로 확인
        # 물건을 버리는 경우의 [가져가는 물건의 가격 합 - 가져가지 않는 물건의 폐기 비용]의 최댓값
        case_dump = dp[i-1][j] - info[i-1][2]
        # 현재 물건을 가져가도 부피의 총량 W를 초과하지 않는 경우(남아있는 부피 >= 추가할 물건의 부피)
        if j >= info[i-1][0]:
            case_bring = dp[i-1][j - info[i-1][0]] + info[i-1][1]
            dp[i][j] = max(case_dump, case_bring)
        else:  # 현재 물건의 부피보다 남아있는 부피의 총량이 작은 경우
            dp[i][j] = case_dump  # 물건을 가져가지 않음

print(dp[N][W])  # 모든 물건들을 순회하고 난 최종 결과 출력