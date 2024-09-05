from collections import deque

def bfs(start_r, start_c, grid, n, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    while queue:
        current_r, current_c = queue.popleft()
        for dr, dc in directions:
            new_r, new_c = current_r + dr, current_c + dc
            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and grid[new_r][new_c] == 0:
                visited[new_r][new_c] = True
                queue.append((new_r, new_c))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0

    n = int(data[index])
    k = int(data[index + 1])
    index += 2

    grid = []
    for _ in range(n):
        grid.append(list(map(int, data[index:index + n])))
        index += n

    starts = []
    for _ in range(k):
        r = int(data[index]) - 1
        c = int(data[index + 1]) - 1
        starts.append((r, c))
        index += 2

    visited = [[False] * n for _ in range(n)]

    for r, c in starts:
        if not visited[r][c]:
            bfs(r, c, grid, n, visited)

    # 방문 가능한 칸 수 계산
    count = sum(sum(row) for row in visited)
    print(count)

if __name__ == "__main__":
    main()