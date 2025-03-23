# 1. 입력으로 양의 정수 (n <= 16) 받음
# 2. 길이가 n인 이진수열 중에서 0이 연속으로 등장하지 않는 이진수열의 개수를 계산


def recursion(prior, idx):
    global cnt

    if idx == N:  # 인덱스가 N이라면
        return  # 함수 탈출

    if prior == 0:  # 앞의 수가 0이라면, 다음에 1만 올 수 있음
        recursion(1, idx+1)  # 1만 올 수 있다면 경우의 수는 그대로 유지
    else:  # 앞의 수가 1이라면, 다음에 0과 1이 올 수 있으므로 cnt + 1
        cnt += 1
        recursion(0, idx+1)
        recursion(1, idx+1)

cnt = 1  # 이진수열의 개수 (N이 양의 정수라고 했으므로 최소 1이다)
N = int(input())

# N이 1일때는 0과 1이 가능하므로 prior(앞의 수)를 1로 지정
# N >= 1 이라면, 이진수열의 가장 큰 자릿수는 1일 수 밖에 없음
recursion(1, 0)
print(cnt)
