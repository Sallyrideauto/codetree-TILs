from collections import deque

def change_direction(direction, cell):
    """
    방향을 바꿔주는 함수
    - direction: 현재 방향 (0=오른쪽, 1=아래, 2=왼쪽, 3=위쪽)
    - cell: 1 또는 2로 구분되는 벽의 종류
    """
    if cell == 1:  # / 벽
        return [3, 2, 1, 0][direction]
    elif cell == 2:  # \ 벽
        return [1, 0, 3, 2][direction]


def simulate(grid, start_row, start_col, start_dir, n):
    """
    구슬의 이동을 시뮬레이션하는 함수
    - grid: 격자 정보
    - start_row, start_col: 시작점 좌표
    - start_dir: 시작 방향
    - n: 격자 크기
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위쪽
    time = 0
    row, col, direction = start_row, start_col, start_dir
    
    while 0 <= row < n and 0 <= col < n:  # 격자 안에 있는 동안 반복
        time += 1
        row += directions[direction][0]
        col += directions[direction][1]
        
        if 0 <= row < n and 0 <= col < n:
            if grid[row][col] == 1 or grid[row][col] == 2:  # 벽을 만난 경우
                direction = change_direction(direction, grid[row][col])
    
    return time + 1  # 마지막 격자를 빠져나가는 시간 포함

def find_max_time(n, grid):
    """
    모든 시작점에 대해 최대 시간을 계산하는 함수
    - n: 격자 크기
    - grid: 격자 정보
    """
    max_time = 0
    
    # 모든 시작점과 방향 탐색 (위, 아래, 왼쪽, 오른쪽 가장자리)
    for i in range(n):
        max_time = max(max_time, simulate(grid, i, 0, 0, n))  # 왼쪽에서 오른쪽
        max_time = max(max_time, simulate(grid, i, n-1, 2, n))  # 오른쪽에서 왼쪽
        max_time = max(max_time, simulate(grid, 0, i, 1, n))  # 위쪽에서 아래쪽
        max_time = max(max_time, simulate(grid, n-1, i, 3, n))  # 아래쪽에서 위쪽
    
    return max_time

# 입력 받기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(find_max_time(n, grid))