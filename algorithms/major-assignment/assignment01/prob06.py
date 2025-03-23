# 1. 길이가 n인 수열이 입력으로 주어짐 (0 ~ 4 정수로만 이루어짐)
# 2. 가장 마지막 원소에 도착하면 성공
# 3. 성공 가능한 수열이라면 Yes, 성공 불가하면 No


def recursion(x):
    if x == N-1:  # 마지막 원소에 도달하면
        return 'Yes'  # 'Yes' 반환

    for i in range(array[x]):  # 1 ~ array[x]만큼 이동가능하므로
        success = recursion(x+i+1)  # recursion(x + (1 ~ array[x])) 호출
        if success == 'Yes':  # 재귀 호출의 결과로 마지막 원소에 도달한다면
            return 'Yes'  # 'Yes' 반환

    return 'No'  # 마지막 원소에 도달하지 못한다면, 'No' 반환

N = int(input())  # N 입력
array = list(map(int, input().split()))  # 길이가 N인 수열 입력

print(recursion(0))  # 0번 인덱스부터 시작하여 재귀적 호출 
