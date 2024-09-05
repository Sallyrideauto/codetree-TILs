def find_next_position(grid, r, c):
    n = len(grid)
    current_value = grid[r][c]
    possible_moves = []

    # 상하좌우를 확인
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] < current_value:
                possible_moves.append((grid[nr][nc], nr, nc))

    # 가능한 이동 중에서 숫자가 가장 큰 칸을 선택
    if possible_moves:
        # 최대값을 가지고 있는 위치 탐색
        # 동일한 값이 있다면 행 번호가 작은 위치, 그 다음으로 열 번호가 작은 위치로 정렬
        return sorted(possible_moves, key=lambda x: (-x[0], x[1], x[2]))[0][1:]

    return None

def simulate_movement(n, k, grid, start_r, start_c):
    r, c = start_r, start_c
    for _ in range(k):
        next_position = find_next_position(grid, r, c)
        if not next_position:
            break
        r, c = next_position
    return r, c

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        grid.append(list(map(int, data[index:index+n])))
        index += n
    
    start_r = int(data[-2]) - 1  # 1-based index를 0-based로 변환
    start_c = int(data[-1]) - 1  # 1-based index를 0-based로 변환

    final_position = simulate_movement(n, k, grid, start_r, start_c)
    print(final_position[0], final_position[1])  # 1-based index로 출력

if __name__ == "__main__":
    main()