from collections import deque

def bfs(grid, start, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동
    queue = deque([start])
    distances = [[float('inf')] * n for _ in range(n)]
    x_start, y_start = start
    distances[x_start][y_start] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#' and distances[nx][ny] == float('inf'):
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
                
    return distances

def solve(grid, n):
    points = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] in 'SE' or grid[i][j].isdigit():
                points[grid[i][j]] = (i, j)

    if 'S' not in points or 'E' not in points or len([k for k in points if k.isdigit()]) < 3:
        return -1

    dist = {p: bfs(grid, points[p], n) for p in points}
    dp = {}
    coin_keys = sorted(k for k in points if k.isdigit())
    start_key = 'S'
    end_key = 'E'
    queue = deque()

    for ck in coin_keys:
        state = (ck, 1 << (ord(ck) - ord('1')))
        dp[state] = dist[start_key][points[ck][0]][points[ck][1]]
        queue.append((ck, state[1], dp[state]))

    while queue:
        last_coin, mask, steps = queue.popleft()

        for next_coin in coin_keys:
            if next_coin > last_coin:
                new_mask = mask | (1 << (ord(next_coin) - ord('1')))
                if dist[last_coin][points[next_coin][0]][points[next_coin][1]] < float('inf'):
                    new_steps = steps + dist[last_coin][points[next_coin][0]][points[next_coin][1]]
                    new_state = (next_coin, new_mask)
                    if new_state not in dp or new_steps < dp[new_state]:
                        dp[new_state] = new_steps
                        queue.append((next_coin, new_mask, new_steps))

    min_steps = float('inf')
    for state in dp:
        last_coin, mask = state
        if bin(mask).count('1') >= 3:
            final_steps = dp[state] + dist[last_coin][points[end_key][0]][points[end_key][1]]
            min_steps = min(min_steps, final_steps)

    return min_steps if min_steps != float('inf') else -1

# 입력을 받는 부분
N = int(input())
grid = []
for _ in range(N):
    grid.append(input().strip())

result = solve(grid, N)
print(result)