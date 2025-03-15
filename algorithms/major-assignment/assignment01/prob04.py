# 1. 출구까지 죽지 않고 갈 수 있는지 결과 출력
# 2. 폭탄 K개 이상 만나면 죽음
# 3. Recursion


route_total = 0  # 총 경로의 개수
maze = []  # 미로 정보
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 4방향 (서북동남)

# 백트래킹 함수
def backtracking(x, y, visited, bomb_cnt):
    global route_total  # 총 경로의 개수 -> 전역변수 선언

    # 출구 도착 && 해당 경로에서 지나친 폭탄의 개수가 K 이하인 경우
    if x == N-1 and y == N-1 and bomb_cnt <= K:
        route_total += 1  # 총 경로의 개수 + 1
        return

    for i in range(4):  # 4방향 탐색
        nx, ny = x + dir[i][0], y + dir[i][1]  # 이동한 x좌표, y좌표 갱신
        # 해당 좌표가 [미로 내부의 범위에 속함 && 방문하지 않음 && 통로]인 경우
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] == 0:
            visited[nx][ny] = 1  # 방문 처리
            backtracking(nx, ny, visited, bomb_cnt)
            visited[nx][ny] = 0  # 방문 미처리
        elif 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] == 2:
            visited[nx][ny] = 1  # 방문 처리
            backtracking(nx, ny, visited, bomb_cnt+1)
            visited[nx][ny] = 0  # 방문 미처리

for _ in range(N := int(input())):  # 미로 정보 입력
    maze.append(list(map(int, input().split())))

K = int(input())  # K 입력 (폭탄 개수)

visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문처리 리스트
visited[0][0] = 1  # 출발 지점(0, 0) 방문 처리

backtracking(0, 0, visited, 0)

if route_total:  # 폭탄 개수의 제한을 넘지 않으면서 출구에 도착할 수 있는 경로의 개수가 1개 이상이라면
    print('Yes')
else:  # 갈 수 있는 경로가 하나도 없다면
    print('No')


# TC 1
# 8
# 0 0 0 2 1 0 0 0
# 0 1 1 0 0 0 1 0
# 0 1 0 1 1 0 2 1
# 0 2 0 2 0 1 0 1
# 0 1 1 0 0 2 1 0
# 2 2 1 0 0 2 1 0
# 0 0 0 1 1 0 0 0
# 0 1 0 0 2 0 1 0
# 2

# TC 2
# 8
# 0 0 0 2 1 0 0 0
# 0 1 1 0 0 0 1 0
# 0 1 0 1 1 0 2 1
# 0 2 0 2 0 1 0 1
# 0 1 1 0 0 2 1 0
# 2 2 1 0 0 2 1 0
# 0 0 0 1 1 0 0 0
# 0 1 0 0 2 0 1 0
# 1

# TC 3
# 4
# 0 2 2 2
# 2 2 2 2
# 2 2 2 2
# 0 2 2 0
# 4

# TC 4
# 5
# 0 0 2 2 2
# 0 2 2 1 2
# 0 1 0 0 0
# 0 2 2 2 0
# 0 0 0 1 0
# 1