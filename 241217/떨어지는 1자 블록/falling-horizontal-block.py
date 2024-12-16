# 입력: n (격자 크기), m (블럭 크기), k (블럭 시작 위치), grid (격자 상태)

def drop_block(n, m, k, grid):
    # 블럭이 떨어질 열들: k부터 k + m - 1 까지
    start_col = k - 1  # 입력 k는 1부터 시작하므로 0-인덱스로 변환
    end_col = start_col + m  # 마지막 열의 범위
    
    # 블럭이 닿을 가장 낮은 위치 찾기
    lowest_row = n  # 처음에는 최저 행으로 초기화
    
    for col in range(start_col, end_col):  # 블럭이 차지하는 열들만 탐색
        for row in range(n):
            if grid[row][col] == 1:  # 기존 블럭과 맞닿으면
                lowest_row = min(lowest_row, row)  # 가장 낮은 행을 업데이트
                break  # 해당 열에서 더 이상 내려갈 수 없음
    
    # 블럭이 안착할 위치의 시작 행 계산
    drop_row = lowest_row - 1  # 블럭의 윗부분이 닿는 위치
    
    # 블럭을 격자판에 배치
    for col in range(start_col, end_col):
        grid[drop_row][col] = 1  # 해당 열의 drop_row에 블럭(1)을 채운다
    
    return grid

# 입력 처리
n, m, k = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 블럭 떨어뜨리기
new_grid = drop_block(n, m, k, grid)

# 결과 출력
for row in new_grid:
    print(" ".join(map(str, row)))
