import copy

def apply_explosion(grid, n, r, c):
    """
    폭탄이 터졌을 때 해당 위치를 중심으로 십자 모양의 숫자를 제거하고 새로운 격자를 반환합니다.
    """
    new_grid = copy.deepcopy(grid)
    bomb_size = grid[r][c]  # 중심 숫자가 폭발 범위 크기
    
    # 중심 폭발 위치
    new_grid[r][c] = 0
    
    # 상하좌우 방향으로 폭발 적용
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상, 하, 좌, 우
        for step in range(1, bomb_size):
            nr, nc = r + dr * step, c + dc * step
            if 0 <= nr < n and 0 <= nc < n:
                new_grid[nr][nc] = 0
    
    return apply_gravity(new_grid, n)

def apply_gravity(grid, n):
    """
    중력을 적용하여 숫자들을 아래로 떨어뜨린 후의 새로운 격자를 반환합니다.
    """
    for col in range(n):
        temp_col = [grid[row][col] for row in range(n) if grid[row][col] != 0]
        temp_col = [0] * (n - len(temp_col)) + temp_col  # 아래로 숫자 떨어짐
        for row in range(n):
            grid[row][col] = temp_col[row]
    return grid

def count_adjacent_pairs(grid, n):
    """
    격자에서 인접한 숫자가 동일한 쌍의 수를 계산합니다.
    """
    count = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                continue
            # 상하좌우 검사
            for dr, dc in [(1, 0), (0, 1)]:  # 아래, 오른쪽만 검사 (중복 방지)
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[r][c] == grid[nr][nc]:
                    count += 1
    return count

def find_best_bomb_location(grid, n):
    """
    폭탄이 터진 후 중력이 작용한 상태에서 최대 쌍의 개수를 만드는 최적의 위치를 찾습니다.
    """
    max_pairs = 0
    for r in range(n):
        for c in range(n):
            # 폭발 시뮬레이션 및 중력 적용
            new_grid = apply_explosion(grid, n, r, c)
            # 인접한 쌍 계산
            pairs = count_adjacent_pairs(new_grid, n)
            # 최대 쌍의 개수 갱신
            max_pairs = max(max_pairs, pairs)
    return max_pairs

def main():
    n = int(input())  # 격자 크기
    grid = [list(map(int, input().split())) for _ in range(n)]
    result = find_best_bomb_location(grid, n)
    print(result)

if __name__ == "__main__":
    main()
