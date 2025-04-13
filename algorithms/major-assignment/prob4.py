import matplotlib.pyplot as plt  # 그래프로 확인 위해 matplotlib 라이브러리 임포트

with open("input.txt", 'r') as f:
    lines = f.readlines()
    point_num = int(lines[0].strip())  # 맨 윗줄에 입력받는 좌표 개수
    points = [list(map(int, line.strip().split())) for line in lines[1:]]  # 좌표들 저장 리스트

# 입력받은 좌표들을 정렬하기 위해, ppt에 나온 분할정복법 알고리즘 사용
# count_and_sort(), merge_and_count()
def count_and_sort(data, s, t):
    if t - s < 1:  # base case - 점이 0개면 반환
        return data[s:t+1]
    else:
        mid = (s + t) // 2
        x = count_and_sort(data, s, mid)
        y = count_and_sort(data, mid + 1, t)
        z, sorted_data = merge_and_count(data, s, mid, t)

        # 실질적으로 사용하는 것은 정렬된 배열인 sorted_data
        # 정렬된 배열들을 data 배열에 새롭게 갱신
        data[s:t+1] = sorted_data

        return data  # 정렬된 배열 전체 반환

# 합병하면서 정렬
def merge_and_count(data, s, mid, t):
    result = []  # 정렬된 좌표들 저장
    i, j = s, mid+1  # 두 배열의 시작점 인덱스 i, j
    cnt = 0  # 두 배열 간의 역전된 쌍 개수 (문제에서 사용X)

    while i <= mid and j <= t:  # 각 배열의 마지막에 도달하기 전까지
        if data[i] <= data[j]:
            result.append(data[i])
            i += 1
        else:
            result.append(data[j])
            j += 1
            # 앞의 배열의 원소가 뒤의 배열의 원소보다 크면 (인덱스 차이 + 1)만큼 역전된 쌍의 개수 증가
            cnt += (mid - i + 1)

    # 나머지 원소 배열에 추가
    result += data[i:mid+1]
    result += data[j:t+1]

    return cnt, result

# 분할
def divide(data, s, t):
    if t - s + 1 <= 3:  # base case - 점이 3개 이하일 때는 더 나누지 않고 반환
        p = data[s:t+1]
        # 좌표 3개로 이루어져 있으면서, 저장된 좌표가 시계 방향이면
        if len(p) == 3 and check_dir(p[0], p[1], p[2]) < 0:
            p[1], p[2] = p[2], p[1]  # 반시계 방향으로 좌표 수정
        return p
    else:
        mid = (s + t) // 2
        left = divide(data, s, mid)  # 왼쪽 convex hull 분할
        right = divide(data, mid+1, t)  # 오른쪽 convex hull 분할

        return merge(left, right)

def merge(left, right):
    q = left.index(max(left, key=lambda x : x[0]))  # 왼쪽 convex hull에서 가장 오른쪽 좌표 인덱스
    p = right.index(min(right, key=lambda x: x[0]))  # 오른쪽 convex hull에서 가장 왼쪽 좌표 인덱스

    # upper/lower line의 두 좌표 각각 저장
    upper_tangent_line, lower_tangent_line = [], []

    # upper tangent line 찾기
    while True:
        shift = False  # 좌표의 이동 여부 확인

        l = (q + 1) % len(left)  # q가 왼쪽 좌표로 이동
        if check_dir(right[p], left[q], left[l]) < 0:  # 시계 방향이면 더 왼쪽으로 이동
            q = l
            shift = True  # 좌표 이동함

        r = (p - 1 + len(right)) % len(right)  # p가 오른쪽 좌표로 이동
        if check_dir(left[q], right[p], right[r]) > 0:  # 반시계 방향이면 더 오른쪽으로 이동
            p = r
            shift = True  # 좌표 이동함

        if not shift:  # q와 p 모두 다른 좌표로 이동하지 않았다면
            upper_tangent_line = [left[q], right[p]]  # q와 p 좌표 확정 및 저장
            break

    q = left.index(max(left, key=lambda x: x[0]))  # 왼쪽 convex hull에서 가장 오른쪽 좌표 인덱스
    p = right.index(min(right, key=lambda x: x[0]))  # 오른쪽 convex hull에서 가장 왼쪽 좌표 인덱스

    # lower tangent line 찾기
    while True:
        shift = False  # 좌표의 이동 여부 확인

        l = (q - 1 + len(left)) % len(left)  # q가 왼쪽 좌표로 이동
        if check_dir(right[p], left[q], left[l]) > 0:  # 반시계 방향이면 더 왼쪽으로 이동
            q = l
            shift = True  # 좌표 이동함

        r = (p + 1) % len(right)  # p가 오른쪽 좌표로 이동
        if check_dir(left[q], right[p], right[r]) < 0:  # 시계 방향이면 더 오른쪽으로 이동
            p = r
            shift = True  # 좌표 이동함

        if not shift:  # q와 p 모두 다른 좌표로 이동하지 않았다면
            lower_tangent_line = [left[q], right[p]]  # q와 p 좌표 확정 및 저장
            break

    # 가장자리 좌표 순서대로 저장
    upper_q = left.index(upper_tangent_line[0])  # upper_tangent_line의 q 좌표
    lower_q = left.index(lower_tangent_line[0])  # lower_tangent_line의 q 좌표
    current_q = upper_q  # upper_q -> lower_q 로 좌표 저장
    edge_points = [left[current_q]]  # upper_q 좌표 저장
    while current_q != lower_q:  # 현재의 좌표가 lower_q와 같지 않는 동안
        current_q = (current_q+1) % len(left)  # 현재의 좌표를 반시계 방향으로 이동
        edge_points.append(left[current_q])  # 좌표 순서대로 저장

    upper_p = right.index(upper_tangent_line[1])  # upper_tangent_line의 p 좌표
    lower_p = right.index(lower_tangent_line[1])  # lower_tangent_line의 p 좌표
    current_p = lower_p  # lower_p -> upper_p 로 좌표 저장
    edge_points.append(right[current_p])  # lower_p 좌표 저장
    while current_p != upper_p:  # 현재의 좌표가 upper_p와 같지 않는 동안
        current_p = (current_p+1) % len(right)  # 현재의 좌표를 반시계 방향으로 이동
        edge_points.append(right[current_p])  # 좌표 순서대로 저장

    return edge_points  # 순서대로 저장된 좌표 리스트 반환

# 방향 확인하는 함수
def check_dir(p0, p1, p2):
    return (p1[0]-p0[0])*(p2[1]-p0[1]) - (p2[0]-p0[0])*(p1[1]-p0[1])

# x좌표를 기준으로 정렬된 좌표 리스트
points = count_and_sort(points, 0, point_num-1)

# 분할정복법으로 convex hull 생성 및 좌표 리스트 반환
convex_hull = divide(points, 0, len(points)-1)

for p in convex_hull:  # 저장된 좌표들을 순서대로 출력
    print(p[0], p[1])



# 그래프로 확인

hull = convex_hull
hull.append(hull[0])

x_all = [p[0] for p in points]
y_all = [p[1] for p in points]
x_hull = [p[0] for p in hull]
y_hull = [p[1] for p in hull]

plt.figure(figsize=(8, 6))
plt.scatter(x_all, y_all, color='blue', label='Points')
plt.plot(x_hull, y_hull, color='red', linewidth=2, label='Convex Hull')
plt.title('Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
