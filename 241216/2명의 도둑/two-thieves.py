from itertools import combinations

# 무게 제한 C를 넘지 않도록 하면서 최대 가치를 구하는 함수
def get_max_value(weight_list, C):
    max_value = 0
    # 모든 가능한 부분 집합을 구함
    for i in range(1, len(weight_list) + 1):
        for subset in combinations(weight_list, i):
            total_weight = sum(subset)
            if total_weight <= C:
                # 가치 = 무게 * 무게
                value = sum(w ** 2 for w in subset)
                max_value = max(max_value, value)
    return max_value

# 두 도둑이 선택할 수 있는 최대 가치를 구하는 함수
def solve_thieves_problem(N, M, C, grid):
    # 각 행마다 가능한 구간과 그 가치를 저장
    row_values = [[] for _ in range(N)]

    for r in range(N):
        for start in range(N - M + 1):  # 가능한 M개의 구간 시작점
            selected_weights = grid[r][start:start + M]
            max_value = get_max_value(selected_weights, C)
            row_values[r].append((start, max_value))  # (시작점, 최대 가치)

    # 두 도둑이 겹치지 않도록 하면서 최대 값을 계산
    max_total_value = 0

    for r1 in range(N):  # 첫 번째 도둑이 선택한 행
        for s1, v1 in row_values[r1]:  # 첫 번째 도둑의 구간
            for r2 in range(N):  # 두 번째 도둑이 선택한 행
                for s2, v2 in row_values[r2]:  # 두 번째 도둑의 구간
                    if r1 != r2 or s1 + M <= s2 or s2 + M <= s1:  # 겹치지 않는 조건
                        max_total_value = max(max_total_value, v1 + v2)
    return max_total_value

# 입력
N, M, C = map(int, input().split())  # 방의 크기 N, 구간 길이 M, 무게 제한 C
grid = [list(map(int, input().split())) for _ in range(N)]  # 각 위치의 물건 무게

# 결과 출력
print(solve_thieves_problem(N, M, C, grid))
