# 수정 필요
def recursion(nums, i, K, cnt):
    if i == len(nums) - 1:
        return cnt
    elif nums[i] < K:
        print(nums[i], cnt)
        return recursion(nums, i+1, K, cnt+1)
    else:
        print(nums[i], cnt)
        return recursion(nums, i+1, K, cnt)

N = int(input())
nums = list(map(int, input().split()))

print(recursion(nums, 0, (K := int(input())), 1))