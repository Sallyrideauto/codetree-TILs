# 주사위의 각 면에 대한 초기 상태
# 주사위의 각 면: [위, 아래, 앞, 뒤, 왼쪽, 오른쪽]
DICE = [1, 6, 2, 5, 4, 3]

# 주사위를 굴리는 함수
def roll_dice(direction, dice):
    top, bottom, front, back, left, right = dice
    if direction == 'L':  # 왼쪽으로 굴릴 때
        return [right, left, front, back, top, bottom]
    elif direction == 'R':  # 오른쪽으로 굴릴 때
        return [left, right, front, back, bottom, top]
    elif direction == 'U':  # 위쪽으로 굴릴 때
        return [front, back, bottom, top, left, right]
    elif direction == 'D':  # 아래쪽으로 굴릴 때
        return [back, front, top, bottom, left, right]
    return dice

# 주사위 이동 방향: (dx, dy)
DIRECTIONS = {
    'L': (0, -1),  # 왼쪽
    'R': (0, 1),   # 오른쪽
    'U': (-1, 0),  # 위쪽
    'D': (1, 0)    # 아래쪽
}

def simulate_dice_moves(n, m, r, c, moves):
    grid = [[0] * n for _ in range(n)]  # n x n 격자판
    dice = DICE[:]  # 주사위 초기 상태 복사
    x, y = r - 1, c - 1  # 초기 위치 (0-indexed)
    
    # 초기 바닥면 숫자 기록
    grid[x][y] = dice[1]

    # 이동 명령 실행
    for move in moves:
        dx, dy = DIRECTIONS[move]  # 이동 방향
        nx, ny = x + dx, y + dy  # 이동 후 위치
        
        # 격자판 밖으로 나가는 경우 무시
        if not (0 <= nx < n and 0 <= ny < n):
            continue

        # 주사위 굴리기
        dice = roll_dice(move, dice)
        
        # 새 위치에 바닥면 숫자 기록
        grid[nx][ny] = dice[1]
        
        # 현재 위치 업데이트
        x, y = nx, ny

    # 격자판에 기록된 숫자들의 총합 계산
    return sum(sum(row) for row in grid)

# 입력 받기
n, m, r, c = map(int, input().split())  # 격자 크기, 이동 횟수, 초기 위치
moves = input().split()  # 이동 명령들

# 결과 출력
result = simulate_dice_moves(n, m, r, c, moves)
print(result)
