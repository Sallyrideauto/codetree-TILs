# 상, 하, 좌, 우 이동을 위한 방향 벡터 정의
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우

dy = [0, 0, -1, 1]  # 상, 하, 좌, 우

def is_valid(nx, ny, n):
    # 격자를 벗어나지 않는지 확인하는 함수
    return 0 <= nx < n and 0 <= ny < n

def move_in_grid(grid, r, c):
    # 방문한 숫자를 저장할 리스트 초기화
    visited_numbers = []
    
    # 시작 위치 숫자를 방문 리스트에 추가
    current_value = grid[r][c]
    visited_numbers.append(current_value)
    
    # 현재 위치를 설정
    x, y = r, c

    while True:
        found_next = False  # 다음 이동할 곳이 있는지 여부
        
        for direction in range(4):  # 상하좌우 순서대로 탐색
            nx = x + dx[direction]  # 이동한 x 좌표
            ny = y + dy[direction]  # 이동한 y 좌표
            
            # 격자를 벗어나지 않고, 현재 숫자보다 큰 숫자인 경우
            if is_valid(nx, ny, len(grid)) and grid[nx][ny] > current_value:
                current_value = grid[nx][ny]  # 새로운 숫자로 갱신
                visited_numbers.append(current_value)  # 방문한 숫자 추가
                x, y = nx, ny  # 위치 이동
                found_next = True  # 다음 위치를 찾았음
                break  # 이동했으므로 반복 종료
                
        if not found_next:  # 이동할 곳이 없으면 종료
            break
    
    return visited_numbers

# 입력 받기
n, r, c = map(int, input().split())  # n: 격자 크기, r: 시작 행, c: 시작 열

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 시작 위치를 0-based index로 조정 (입력은 1-based)
r -= 1
c -= 1

# 함수 실행 및 결과 출력
result = move_in_grid(grid, r, c)
print(" ".join(map(str, result)))
