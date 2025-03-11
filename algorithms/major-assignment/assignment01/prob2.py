# 1. 입력받은 정수들 중에서 K와 가장 가까운 정수를 찾는 함수 nearest
# 2. 답이 2개 이상이라면, 그 중 작은 값 출력
# 3. 함수 nearest의 시간 복잡도는 O(log N)
# 4. N개의 정수들을 배열에 저장하는 것 외에는 반복문 사용 금지


def nearest(start, end, near_nums, diff):
    if start <= end:  # start가 end보다 작거나 같을 때
        mid = (start + end) // 2  # mid

        if abs(nums[mid] - K) == diff:  # K와의 차이가 현재까지 가장 작은 차이(diff)와 같은 경우
            near_nums.append(nums[mid])  # nums[mid] 값 추가
        elif abs(nums[mid] - K) < diff:  # K와의 차이가 현재까지 가장 작은 차이(diff)보다 작은 경우
            near_nums = [nums[mid]]  # near_nums 리스트 갱신, nums[mid] 값 저장
            diff = abs(nums[mid] - K)  # 현재까지 가장 작은 차이(diff) 갱신

        if nums[mid] < K:  # mid 위치의 값이 K보다 작은 경우
            return nearest(mid+1, end, near_nums, diff)  # start = mid + 1
        elif nums[mid] == K:  # mid 위치의 값이 K와 같은 경우
            return min(near_nums)  # near_nums의 가장 작은 값 반환
        else:  # mid 위치의 값이 K보다 큰 경우
            return nearest(start, mid-1, near_nums, diff)  # end = mid - 1
    else:  # start > end 인 경우
        return min(near_nums)  # near_nums의 최솟값 반환


global nums, near_nums  # 전역변수 선언
N = int(input())
nums = list(map(int, input().split()))
K = int(input())

print(nearest(0, N-1, [], float("inf")))