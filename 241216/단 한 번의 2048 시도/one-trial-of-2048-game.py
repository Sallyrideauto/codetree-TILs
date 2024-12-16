def compress_and_merge(row):
    # 0을 제외하고 숫자를 왼쪽으로 밀어붙임
    new_row = [num for num in row if num != 0]
    merged_row = []
    i = 0
    while i < len(new_row):
        # 현재 숫자와 다음 숫자가 같으면 합침
        if i < len(new_row) - 1 and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            i += 2  # 합쳐진 경우 다음 숫자로 건너뜀
        else:
            merged_row.append(new_row[i])
            i += 1
    # 합쳐진 숫자 뒤에 0을 채워서 길이 4로 맞춤
    while len(merged_row) < 4:
        merged_row.append(0)
    return merged_row

def move_left(board):
    return [compress_and_merge(row) for row in board]

def move_right(board):
    return [compress_and_merge(row[::-1])[::-1] for row in board]

def move_up(board):
    rotated = list(zip(*board))  # 행과 열을 바꿔서 세로를 가로처럼 처리
    moved = move_left(rotated)
    return [list(row) for row in zip(*moved)]

def move_down(board):
    rotated = list(zip(*board))
    moved = move_right(rotated)
    return [list(row) for row in zip(*moved)]

def play_2048(board, direction):
    if direction == 'L':
        return move_left(board)
    elif direction == 'R':
        return move_right(board)
    elif direction == 'U':
        return move_up(board)
    elif direction == 'D':
        return move_down(board)

# 입력
board = [list(map(int, input().split())) for _ in range(4)]
direction = input().strip()

# 결과 계산
result = play_2048(board, direction)

# 출력
for row in result:
    print(" ".join(map(str, row)))
