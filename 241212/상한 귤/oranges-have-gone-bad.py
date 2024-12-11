from collections import deque

# 입력 처리
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 리스트 초기화
result = [[-1 if grid[i][j] == 0 else -2 for j in range(n)] for i in range(n)]

# BFS 초기화
queue = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:  # 초기 상한 귤 위치
            queue.append((i, j, 0))  # (행, 열, 시간)
            result[i][j] = 0  # 상한 귤의 시간은 0으로 초기화

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색
while queue:
    x, y, time = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            # 상한 귤로 전이
            grid[nx][ny] = 2
            result[nx][ny] = time + 1
            queue.append((nx, ny, time + 1))

# 출력 결과 구성
for row in result:
    print(' '.join(map(str, row)))
