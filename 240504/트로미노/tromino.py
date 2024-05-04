def max_block_sum(n, m, grid):
    # 정의된 블록 방향
    L_orientations = [
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # 정상
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # 90도 회전
        [(0, 1), (1, 1), (2, 1), (2, 0)],  # 180도 회전
        [(1, 0), (1, 1), (1, 2), (0, 0)]   # 270도 회전
    ]
    linear_orientations = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # 수평
        [(0, 0), (1, 0), (2, 0), (3, 0)]  # 수직
    ]
    
    max_sum = 0

    def calculate_sum(x, y, block):
        s = 0
        for dx, dy in block:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return 0
            s += grid[nx][ny]
        return s

    for block in L_orientations + linear_orientations:
        for i in range(n):
            for j in range(m):
                current_sum = calculate_sum(i, j, block)
                if current_sum > max_sum:
                    max_sum = current_sum

    return max_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n, m = int(data[0]), int(data[1])
    grid = []
    index = 2
    for _ in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m

    # 결과 출력
    print(max_block_sum(n, m, grid))

if __name__ == "__main__":
    main()