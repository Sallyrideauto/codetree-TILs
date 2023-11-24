from collections import deque

def bfs(grid, start, end, block):
    # 격자 크기
    n = 10

    # 방문한 위치를 추적하기 위한 배열
    visited = [[False] * n for _ in range(n)]

    # 탐색을 위한 큐
    queue = deque([(start, -1)])  # (위치, 거리 시작을 -1로)
    visited[start[0]][start[1]] = True

    # 너비 우선 탐색
    while queue:
        (x, y), dist = queue.popleft()

        # 목표 위치에 도달했을 때
        if (x, y) == end:
            return dist

        # 상하좌우 이동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # 격자 내부이고, 방문하지 않았으며, 'R'을 피해야 하는 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (nx, ny) != block:
                visited[nx][ny] = True
                queue.append(((nx, ny), dist + 1))

    # 목표 위치에 도달할 수 없는 경우
    return -1

# 입력 처리
grid = []
for _ in range(10):
    grid.append(list(input()))

# L, R, B 위치 찾기
l_pos, r_pos, b_pos = None, None, None
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'L':
            l_pos = (i, j)
        elif grid[i][j] == 'R':
            r_pos = (i, j)
        elif grid[i][j] == 'B':
            b_pos = (i, j)

# BFS를 사용하여 최단거리 계산
distance = bfs(grid, l_pos, b_pos, r_pos)
print(distance)