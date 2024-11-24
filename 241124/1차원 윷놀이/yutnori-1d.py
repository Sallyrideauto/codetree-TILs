from itertools import product

def max_score(n, m, k, moves):
    max_points = 0
    # 각 턴마다 말을 선택하는 모든 가능한 경우의 수 생성
    for choice in product(range(k), repeat=n):
        positions = [1] * k  # 모든 말의 시작 위치는 1번
        points = 0
        for turn in range(n):
            selected_piece = choice[turn]
            if positions[selected_piece] < m:
                positions[selected_piece] += moves[turn]
                if positions[selected_piece] >= m:
                    positions[selected_piece] = m
                    points += 1
        max_points = max(max_points, points)
    return max_points

# 입력 받기
n, m, k = map(int, input().split())
moves = list(map(int, input().split()))

# 최대 점수 계산 및 출력
print(max_score(n, m, k, moves))