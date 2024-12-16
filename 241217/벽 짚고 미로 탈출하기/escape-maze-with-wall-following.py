# 방향: 오른쪽(0), 아래(1), 왼쪽(2), 위쪽(3)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(nx, ny, N, maze):
    return 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != '#'

def escape_maze(N, start_x, start_y, maze):
    x, y = start_x - 1, start_y - 1  # 시작 위치 (0-indexed)
    direction = 0  # 처음에는 오른쪽(0)을 바라봄
    visited = set()  # 방문 기록
    time = 0  # 경과 시간

    while True:
        # 무한 루프에 빠지지 않기 위해 시작점과 방향의 반복을 확인
        if (x, y, direction) in visited:
            return -1  # 탈출 불가
        visited.add((x, y, direction))

        # 현재 바라보는 방향
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        # 1. 현재 방향으로 나갈 수 있다면 탈출
        if not (0 <= nx < N and 0 <= ny < N):
            return time + 1  # 격자 밖으로 나가면 탈출 성공

        # 2. 현재 방향이 벽이라면 반시계 방향 회전
        if not is_valid(nx, ny, N, maze):
            direction = (direction + 3) % 4  # 반시계 방향 회전
            continue

        # 3. 오른쪽 벽이 존재하는지 확인
        right_direction = (direction + 1) % 4
        rx, ry = x + directions[right_direction][0], y + directions[right_direction][1]

        # 4. 오른쪽 벽이 있으면 현재 방향으로 이동
        if is_valid(rx, ry, N, maze):
            x, y = nx, ny
            time += 1
        else:
            # 오른쪽 벽이 없으면 이동하고 시계 방향 회전
            x, y = nx, ny
            direction = right_direction
            time += 1

# 입력 처리
N = int(input())
x, y = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

# 결과 출력
result = escape_maze(N, x, y, maze)
print(result)
