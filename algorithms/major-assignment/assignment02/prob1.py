import time
import sys
sys.setrecursionlimit(10**8)

with open("harry_full.txt", 'r') as f:
    words = f.read().split()

# 1. 버블 정렬 - 1824.17202 sec
def bubble_sort(arr):
    for i in range(n := len(arr)):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 2. 삽입 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

# 3. 합병 정렬 - 1.29161 sec
def merge_sort(arr):
    # base case
    if len(arr) <= 1:  # 배열의 길이가 1이 되면, 더 이상 쪼개지 않고 반환
        return arr

    mid = len(arr) // 2
    left = arr[:mid]  # mid를 기준으로 왼쪽 배열
    right = arr[mid:]  # mid를 기준으로 오른쪽 배열

    left = merge_sort(left)  # left와 right를 재귀적으로 정렬
    right = merge_sort(right)

    return merge(left, right)  # 정렬된 left와 right를 합치기

# 두 배열을 합치는 함수
def merge(left, right):
    result = []  # 두 배열을 합친 결과를 담는 리스트
    i, j = 0, 0  # left와 right를 순회할 인덱스를 0으로 초기화 (맨 앞부터 탐색)

    # 두 배열 중 한 배열의 모든 요소를 result에 담을 동안
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # left의 원소가 right보다 작으면
            result.append(left[i])  # result에 더 작은 수인 left의 원소 추가
            i += 1  # left의 인덱스 + 1
        else:
            result.append(right[j])  # result에 더 작은 수인 right의 원소 추가
            j += 1  # right의 인덱스 + 1

    # left와 right 중 하나는 모든 요소를 result에 담았지만,
    # 다른 배열은 다 넣지 못한 상태이므로
    # result에 담지 않은 나머지 요소들 전부 추가
    result += left[i:]
    result += right[j:]

    return result

# 4. 빠른 정렬 - 19.61268 sec
def quick_sort(arr, start, end):

    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)

    return arr

def partition(arr, start, end):
    p = end

    left = start - 1

    for right in range(start, end):
        if arr[right] <= arr[p]:
            left += 1
            arr[left], arr[right] = arr[right], arr[left]
    arr[p], arr[left+1] = arr[left+1], arr[p]

    return left + 1

# 5. 힙정렬 - 1.48823 sec
def heap_sort(arr):
    # 처음에 전체 힙 만들기
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i, len(arr))

    # root 노드와 마지막 노드를 바꾸고 나서
    # root 노드를 기준으로 heapify 실행
    for r in range(len(arr)-1, 0, -1):
        arr[0], arr[r] = arr[r], arr[0]
        heapify(arr, 0, r-1)

    return arr

# heapify 함수
def heapify(arr, parent, n):
    bigger = parent  # 가장 큰 노드의 인덱스
    left = parent * 2 + 1  # 왼쪽 자식 노드의 인덱스
    right = parent * 2 + 2  # 오른쪽 자식 노드의 인덱스

    if left < n and arr[left] > arr[bigger]:  # 왼쪽 자식 노드 > 부모 노드
        bigger = left  # 가장 큰 노드를 왼쪽 자식 노드로 갱신

    if right < n and arr[right] > arr[bigger]:  # 오른쪽 자식 노드 > 가장 큰 노드(부모/왼쪽)
        bigger = right  # 가장 큰 노드를 오른쪽 자식 노드로 갱신

    if bigger != parent:  # 가장 큰 노드가 부모 노드가 아니라면
        arr[parent], arr[bigger] = arr[bigger], arr[parent]  # 가장 큰 노드와 부모 노드는 swap
        heapify(arr, bigger, n)  # 바뀐 자식 노드를 기준으로 heapify

# 6. 라이브러리 제공 정렬 알고리즘 - 0.09279 sec
def sort(arr):
    return arr.sort()


start = time.time()
# insertion_sort(words)
# merge_sort(words)
# quick_sort(words, 0, len(words)-1)
heap_sort(words)
# sort(words)
end = time.time()
print(f"{end - start:.5f} sec")

