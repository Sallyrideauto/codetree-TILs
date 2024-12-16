def apply_gravity(box, N):
    """
    중력을 적용하여 폭탄을 아래로 내리는 함수
    """
    for col in range(N):
        temp_col = []
        for row in range(N):
            if box[row][col] != 0:  # 폭탄이 있으면 저장
                temp_col.append(box[row][col])
        # 남은 폭탄을 밑으로 채우고 나머지는 0으로 채움
        for row in range(N):
            if row < N - len(temp_col):
                box[row][col] = 0
            else:
                box[row][col] = temp_col[row - (N - len(temp_col))]

def find_and_burst(box, N, M):
    """
    연속된 M개 이상의 같은 숫자가 있는 폭탄을 찾아 터뜨리는 함수
    """
    to_burst = set()
    for col in range(N):
        count = 0
        for row in range(1, N):
            if box[row][col] == box[row-1][col] and box[row][col] != 0:
                count += 1
            else:
                if count >= M:
                    for r in range(row - count, row):
                        to_burst.add((r, col))
                count = 1
        # 끝까지 연속 확인
        if count >= M:
            for r in range(N - count, N):
                to_burst.add((r, col))

    for r, c in to_burst:
        box[r][c] = 0  # 터뜨림
    return len(to_burst) > 0  # 터진 폭탄이 있으면 True 반환

def rotate_90_clockwise(box, N):
    """
    상자를 시계방향으로 90도 회전시키는 함수
    """
    new_box = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_box[col][N - 1 - row] = box[row][col]
    return new_box

def count_bombs(box, N):
    """
    남아 있는 폭탄의 개수를 세는 함수
    """
    return sum(row.count(0) == False for row in box)

def bomb_simulation(N, M, K, box):
    """
    주어진 조건에 맞게 폭탄을 처리하는 메인 함수
    """
    for _ in range(K):
        while True:
            if not find_and_burst(box, N, M):
                break  # 터질 폭탄이 없으면 중단
            apply_gravity(box, N)  # 중력 적용
        box = rotate_90_clockwise(box, N)  # 시계방향 회전
    # 마지막 회전 이후에도 터질 폭탄이 있는지 확인
    while True:
        if not find_and_burst(box, N, M):
            break
        apply_gravity(box, N)
    return count_bombs(box, N)

# 입력 받기
N, M, K = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = bomb_simulation(N, M, K, box)
print(result)
