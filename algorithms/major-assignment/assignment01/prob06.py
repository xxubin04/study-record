# 1. 길이가 n인 수열이 입력으로 주어짐 (0 ~ 4 정수로만 이루어짐)
# 2. 가장 마지막 원소에 도착하면 성공
# 3. 성공 가능한 수열이라면 Yes, 성공 불가하면 No


def recursion(x):
    if x == N-1:
        return 'Yes'

    for i in range(array[x]):
        success = recursion(x+i+1)
        if success == 'Yes':
            return 'Yes'

    return 'No'

N = int(input())
array = list(map(int, input().split()))

print(recursion(0))


# TC 1
# 8
# 2 3 1 0 2 0 1 3

# TC 2
# 14
# 3 1 0 2 4 2 1 0 3 0 3 1 0 1

# TC 3
# 8
# 2 4 3 2 1 0 4 3

# TC 4
# 5
# 2 1 0 2 3