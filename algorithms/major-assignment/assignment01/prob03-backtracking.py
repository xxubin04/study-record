# 1. 미로 찾기 문제
# 2. 길이가 K 이하인 서로 다른 경로의 개수
# 3. Recursion
# 4. 같은 위치를 2번 이상 방문하면 안됨


route_length = 0  # 특정 경로의 길이
route_total = 0  # 총 경로의 개수
maze = []  # 미로 정보
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 4방향 (서북동남)

# 백트래킹 함수
def backtracking(x, y, visited, route_length):
    global route_total  # 총 경로의 개수 -> 전역변수 선언

    if x == N-1 and y == N-1 and route_length <= K:  # 출구 도착 && 경로의 길이가 K 이하인 경우
        route_total += 1  # 총 경로의 개수 + 1
        return

    for i in range(4):  # 4방향 탐색
        nx, ny = x + dir[i][0], y + dir[i][1]  # 이동한 x좌표, y좌표 갱신
        # 해당 좌표가 [미로 내부의 범위에 속함 && 방문하지 않음 && 통로]인 경우
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] == 0:
            visited[nx][ny] = 1  # 방문 처리
            backtracking(nx, ny, visited, route_length+1)  # 백트래킹 재귀호출
            visited[nx][ny] = 0  # 방문 미처리

for _ in range(N := int(input())):  # 미로 정보 입력
    maze.append(list(map(int, input().split())))

K = int(input())  # K 입력

visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문처리 리스트
visited[0][0] = 1  # 출발 지점(0, 0) 방문 처리

backtracking(0, 0, visited, route_length)  # 백트래킹 호출
print(route_total)  # 총 경로의 개수 출력



# TC 1
# 8
# 0 0 0 0 1 0 0 0
# 0 1 1 0 0 0 1 0
# 0 1 0 1 1 0 0 1
# 0 0 0 0 1 1 1 0
# 0 1 1 0 1 0 0 0
# 0 0 1 0 0 0 1 0
# 0 0 0 1 1 0 0 0
# 0 1 0 0 0 0 1 0
# 20

# TC 2
# 3
# 0 0 0
# 0 0 0
# 0 0 0
# 8

# TC 3
# 3
# 0 0 0
# 0 0 0
# 0 0 0
# 7

# TC 4
# 3
# 0 0 0
# 0 1 0
# 0 0 0
# 10

# TC 5
# 4
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 8

# TC 6
# 5
# 0 0 0 0 0
# 0 0 0 1 0
# 0 1 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 10