from itertools import combinations
from collections import deque

def bfs(start, grid, n, u, d):
    # BFS를 이용해 갈 수 있는 도시의 수를 계산합니다.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * n for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                height_diff = abs(grid[nx][ny] - grid[x][y])
                if u <= height_diff <= d:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count, visited

def max_reachable_cities(n, k, u, d, grid):
    # 가능한 모든 k개의 도시 조합을 구합니다.
    cities = [(i, j) for i in range(n) for j in range(n)]
    max_count = 0

    for selected_cities in combinations(cities, k):
        total_visited = set()
        for city in selected_cities:
            # 각 도시에서 BFS를 실행합니다.
            _, visited = bfs(city, grid, n, u, d)
            for i in range(n):
                for j in range(n):
                    if visited[i][j]:
                        total_visited.add((i, j))

        # 총 방문할 수 있는 도시의 수를 계산합니다.
        max_count = max(max_count, len(total_visited))

    return max_count

# 입력 처리
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_reachable_cities(n, k, u, d, grid))
