# 1. K의 rank = N개의 정수 중에서 K보다 작은 것의 개수 + 1
# 2. 배열 저장 로직 외에 반복문 사용 금지
# 3. 시간복잡도 O(N) 초과 X


cnt = 0
N = int(input())
not_yet_K = True  # K 입력의 유무
smaller_than_K = []  # K보다 작은 값들 저장

for num in map(int, input().split()):  # 숫자들을 입력받고 각각의 숫자 순회
    if not_yet_K:  # 아직 K가 입력되지 않았다면 K 입력
        K = int(input())
        not_yet_K = False
    if num < K:  # 숫자가 K보다 작으면 리스트에 저장
        smaller_than_K.append(num)

print(len(smaller_than_K)+1)  # 저장된 숫자들의 개수 + 1

# TC 1
# 10
# 2 5 3 8 6 7 8 7 2 1
# 8

# TC 2
# 25
# 88 1 9 99 24 99 1 45 17 21 23 73 31 37 6 38 9 91 3 99 47 58 55 73 51
# 50

# TC 3
# 8
# 1 1 1 1 2 2 2 2
# 2