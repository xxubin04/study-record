import random
import time

array1 = [random.randint(0, 100000) for _ in range(100000)]
array2 = array1  # 최대한 공정한 비교를 하기 위해 같은 배열 2개 생성

# 1. 정렬되지 않은 배열 사용 - 386.26355 sec
def implement_by_array(arr):
    for _ in range(100000):
        cal = random.randint(0, 1)  # 0: 삽입 / 1: 최댓값 삭제

        if cal == 0:  # 0: 삽입 연산
            arr.append(random.randint(0, 100000))  # 랜덤 값을 배열의 맨 끝에 추가
        else:  # 1: 최댓값 삭제 연산
            max_num = 0
            for i in range(len(arr)):  # O(N) 시간 안에 최댓값 찾기
                if arr[i] > max_num:
                    max_num = arr[i]
            arr.remove(max_num)  # 배열에서 최댓값 삭제


# 2. 우선순위큐 사용 - 0.27672 sec
heap_last_idx = 99999  # 힙의 마지막 원소의 인덱스 값

def priority_queue(arr, heap_last_idx):
    build_max_heap(arr)  # 처음에 힙 정렬

    for _ in range(100000):
        cal = random.randint(0, 1)  # 0: 삽입 / 1: 최댓값 삭제

        if cal == 0:
            # 랜덤 값을 배열의 맨 끝에 추가하고 heapify
            max_heap_insert(arr, random.randint(0, 100000))
            heap_last_idx += 1  # heap_last_idx 1 증가
        else:
            heap_last_idx = extract_max(arr, heap_last_idx)  # 최댓값 삭제 및 힙의 마지막 인덱스 갱신

# 새로운 값 삽입 함수
def max_heap_insert(arr, insert_num):
    arr.append(insert_num)  # 힙의 마지막 노드에 값 추가
    problem_idx = len(arr) - 1

    # 문제 노드가 루트 노드가 아니면서, 부모 노드보다 큰 경우
    while problem_idx > 0 and arr[parent_idx := (problem_idx // 2)] < arr[problem_idx]:
        arr[parent_idx], arr[problem_idx] = arr[problem_idx], arr[parent_idx]  # 부모 노드와 문제 노드 swap
        problem_idx = parent_idx  # 문제 노드는 이제 부모 노드가 됨

# 최댓값 삭제 함수
def extract_max(arr, heap_last_idx):
    arr[0], arr[heap_last_idx] = arr[heap_last_idx], arr[0]  # 최댓값(arr[0])과 마지막 원소(arr[heap_last_idx]) swap
    heapify(arr, 0, heap_last_idx)  # 루트 노드 heapify

    return heap_last_idx - 1  # 마지막 원소 제거 (최댓값 삭제)

# 힙 정렬 함수
def build_max_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr)-1)


# heapify 함수
def heapify(arr, parent, n):
    bigger = parent  # 가장 큰 노드의 인덱스
    left = parent * 2 + 1  # 왼쪽 자식 노드의 인덱스
    right = parent * 2 + 2  # 오른쪽 자식 노드의 인덱스

    if left <= n and arr[left] > arr[bigger]:  # 왼쪽 자식 노드 > 부모 노드
        bigger = left  # 가장 큰 노드를 왼쪽 자식 노드로 갱신

    if right <= n and arr[right] > arr[bigger]:  # 오른쪽 자식 노드 > 가장 큰 노드(부모/왼쪽)
        bigger = right  # 가장 큰 노드를 오른쪽 자식 노드로 갱신

    if bigger != parent:  # 가장 큰 노드가 부모 노드가 아니라면
        arr[parent], arr[bigger] = arr[bigger], arr[parent]  # 가장 큰 노드와 부모 노드는 swap
        heapify(arr, bigger, n)  # 바뀐 자식 노드를 기준으로 heapify


# start = time.time()
# implement_by_array(array1)
# end = time.time()
# print(f"{end - start:.5f} sec")

start = time.time()
priority_queue(array2, heap_last_idx)
end = time.time()
print(f"{end - start:.5f} sec")