from collections import deque

def bfs(grid, start, shelters, n):
    queue = deque([start])
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    distance = [[-1] * n for _ in range(n)]
    distance[start[0]][start[1]] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_dist = float('inf')

    while queue:
        x, y = queue.popleft()

        if grid[x][y] == 3:  # Reached a shelter
            min_dist = min(min_dist, distance[x][y])
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return min_dist if min_dist != float('inf') else -1

def find_min_distances(n, h, m, grid):
    result = [[0] * n for _ in range(n)]
    people = []
    shelters = []

    # Collect all people and shelters positions
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                people.append((i, j))
            elif grid[i][j] == 3:
                shelters.append((i, j))

    # Compute minimum distance for each person to a shelter
    for person in people:
        result[person[0]][person[1]] = bfs(grid, person, shelters, n)

    return result

# Input handling
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Find minimum distances
result = find_min_distances(n, h, m, grid)

# Output result
for row in result:
    print(" ".join(map(str, row)))
