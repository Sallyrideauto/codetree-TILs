from collections import deque
import sys
input = sys.stdin.read

def bfs(grid, visited, start, n):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    num = grid[start[0]][start[1]]
    count = 0

    while queue:
        x, y = queue.popleft()
        count += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == num:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return count

def find_explosive_blocks(n, grid):
    visited = [[False] * n for _ in range(n)]
    explosive_count = 0
    max_block_size = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                block_size = bfs(grid, visited, (i, j), n)
                if block_size >= 4:
                    explosive_count += 1
                    max_block_size = max(max_block_size, block_size)

    return explosive_count, max_block_size

def main():
    data = input().split()
    n = int(data[0])
    grid = []

    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        grid.append(row)
        index += n

    explosive_count, max_block_size = find_explosive_blocks(n, grid)
    print(explosive_count, max_block_size)

if __name__ == "__main__":
    main()