def dfs(x, y, n, grid, visited):
    # 이동 가능한 방향: 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    cnt = 0

    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True

        # 현재 위치에 사람이 있을 경우 카운트 증가
        cnt += 1

        # 인접한 칸 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                stack.append((nx, ny))

    return cnt

def cnt_villages(n, grid):
    visited = [[False] * n for _ in range(n)]
    village_sizes = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                size = dfs(i, j, n, grid, visited)
                village_sizes.append(size)

    village_sizes.sort()
    return len(village_sizes), village_sizes

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 마을 개수 및 크기 계산
village_cnt, village_sizes = cnt_villages(n, grid)

print(village_cnt)
for size in village_sizes:
    print(size)