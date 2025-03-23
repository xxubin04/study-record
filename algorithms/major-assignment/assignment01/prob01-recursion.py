def recursion(arr, i, k, cnt):
    if i == len(arr):  # 배열의 모든 정수를 탐색했다면
        return cnt  # cnt 반환
    elif arr[i] < k:  # 정수가 K보다 작다면
        return recursion(arr, i+1, k, cnt+1)  # cnt 1 증가
    else:  # 정수가 K보다 크거나 같다면
        return recursion(arr, i+1, k, cnt)  # cnt 유지

N = int(input())  # 정수 개수 N 입력
nums = list(map(int, input().split()))  # 정수들을 배열에 입력

# 인덱스 0번부터, cnt를 1로 설정하여 재귀적으로 탐색 시작
print(recursion(nums, 0, (K := int(input())), 1))
