from collections import deque

def can_escape(n, m, grid):
    # 이동 방향: 아래, 오른쪽
    directions = [(1, 0), (0, 1)]

    # BFS 초기화
    queue = deque([(0, 0)]) # 시작점 (0, 0)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        # 도착점에 도달했는지 확인
        if x == n - 1 and y == m - 1:
            return 1

        # 인접한 칸으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 유효한 범위 내에 있고, 뱀이 없으며 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return 0    # 도착점에 도달할 수 없는 경우

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

print(can_escape(n, m, grid))