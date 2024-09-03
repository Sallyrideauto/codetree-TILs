def read_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    N, M = int(data[0]), int(data[1])
    heights = []
    index = 2
    for _ in range(N):
        heights.append(list(map(int, data[index:index + M])))
        index += M
    return N, M, heights

def find_safe_areas(N, M, heights, rain_level):
    visited = [[False] * M for _ in range(N)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and heights[nx][ny] > rain_level:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    area_count = 0
    for i in range(N):
        for j in range(M):
            if heights[i][j] > rain_level and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                area_count += 1

    return area_count

def main():
    N, M, heights = read_input()
    max_height = max(max(row) for row in heights)

    max_areas = 0
    best_k = 0
    for k in range(1, max_height + 1):
        safe_areas = find_safe_areas(N, M, heights, k)
        if safe_areas > max_areas:
            max_areas = safe_areas
            best_k = k

    print(best_k, max_areas)

if __name__ == "__main__":
    main()