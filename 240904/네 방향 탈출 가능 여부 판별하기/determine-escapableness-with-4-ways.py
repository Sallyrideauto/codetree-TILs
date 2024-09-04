from collections import deque

def can_escape(grid, n, m):
    # 상하좌우 이동을 위한 방향 벡처
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 방문 여부를 기록하는 배열
    visited = [[False] * m for _ in range(n)]
    # BFS를 위한 큐
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        # 목적지 도달 시
        if x == n - 1 and y == m - 1:
            return 1
        # 상하좌우 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 이동 가능한 위치인지 확인
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return 0

n, m = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

print(can_escape(grid, n, m))