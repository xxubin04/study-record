# 1. 미로 찾기 문제
# 2. 길이가 K 이하인 서로 다른 경로의 개수
# 3. Recursion
# 4. 같은 위치를 2번 이상 방문하면 안됨


route_total = 0  # 총 경로의 개수
maze = []  # 미로 정보 리스트

nx = [-1, 0, 1, 0]  # 4방향 이동 정보 (서북동남)
ny = [0, -1, 0, 1]

# DFS 함수
def dfs(maze, x, y, visited, route_length):
    global route_total  # 총 경로의 개수 -> 전역 변수 선언
    visited[x][y] = 1  # 방문 처리

    if x == N-1 and y == N-1 and route_length <= K:  # 도착 지점 && 경로의 길이가 K 이하
        route_total += 1  # 총 경로의 개수 + 1

    for i in range(4):  # 4방향 탐색
        dx, dy = x + nx[i], y + ny[i]  # x좌표, y좌표 갱신
        # 해당 좌표가 [미로 내부의 범위 && 방문 X && 통로]인 경우
        if 0 <= dx < N and 0 <= dy < N and visited[dx][dy] == 0 and maze[dx][dy] == 0:
            dfs(maze, dx, dy, visited, route_length+1)  # dfs함수 재귀 호출

    visited[x][y] = 0  # 방문 미처리

for _ in range(N := int(input())):  # 미로 정보 입력
    maze.append(list(map(int, input().split())))

K = int(input())  # K 입력

visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문 처리
dfs(maze, 0, 0, visited, 0)  # dfs 호출

print(route_total)  # 총 경로의 개수 출력