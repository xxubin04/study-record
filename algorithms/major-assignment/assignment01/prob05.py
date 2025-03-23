# 1. N x N 크기의 미로
# 2. 한 번에 최대 K칸만큼 이동 가능
# 3. 한 번 이동하면, 반드시 휴식을 취해야 함
# 4. 출구에 도착하는 경로들 중 최소의 휴식 횟수를 출력
# 5. 출구까지 가는 경로가 없다면, -1 출력


from collections import deque

# maze.txt 입력파일 읽어오기
filename = 'maze.txt'
f = open(filename, 'r')
lines = f.readlines()
maze = []
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 4방향 (서북동남)

for i in range(len(lines)):  # idx에 따라 N, maze, K 값 할당
    if i == 0:
        N = int(lines[i].rstrip())
    elif i == len(lines)-1:
        K = int(lines[i].rstrip())
    else:
        maze.append(list(map(int, lines[i].rstrip().split())))

# 방문 처리 리스트
# visited에 각 좌표마다 휴식횟수로 값을 갱신할 것이므로 999999999로 초기화
visited = [[999999999 for _ in range(N)] for _ in range(N)]

def bfs(maze):
    q = deque([(0, 0, 0)])  # (x좌표, y좌표, 특정 지점에서의 휴식횟수) 저장하는 큐
    visited[0][0] = 0  # 시작할 때는 휴식횟수가 0이므로 0으로 방문 처리

    while q:
        x, y, rest_cnt = q.popleft()  # x좌표, y좌표, 휴식횟수

        if x == N-1 and y == N-1:  # 도착지점에 도착한 경우
            return rest_cnt

        for dx, dy in dir:  # 4방향(서북동남) 탐색
            for n in range(1, K+1):  # 일직선으로 1 ~ K칸 이동 가능
                nx, ny = x + dx * n, y + dy * n  # 이동한 후의 x좌표, y좌표
                # 범위 밖의 좌표라면 탈출
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                # 벽이라면 break
                # 벽일 때 break하지 않으면, 벽을 넘어서 이동하는 것이므로 조건 만족 X
                if maze[nx][ny] == 1:
                    break
                # 범위 안 + 이동가능 + 현재까지의 휴식 횟수가 기록된 최소 휴식 횟수보다 작을 때
                # 해당 좌표에서의 휴식 횟수를 갱신해주고, 큐에 추가
                if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 0 and visited[nx][ny] > rest_cnt + 1:
                    visited[nx][ny] = rest_cnt + 1
                    q.append((nx, ny, rest_cnt + 1))

    return -1  # 도착지점에 도달하지 못한다면, -1 반환

print(bfs(maze))
