import itertools

def find_max_min_value(grid, n):
    # 가능한 열 선택의 모든 순열을 생성
    cols_permutations = itertools.permutations(range(n))

    # 색칠된 칸들의 최소값을 최대화하기 위한 변수
    max_min_value = 0

    # 각 열의 순열에 대해 계산
    for perm in cols_permutations:
        # 현재 순열에서 선택된 칸의 값을 저장할 리스트
        selected_values = []

        # 각 행에 대해 색칠된 칸의 값을 선택
        for row in range(n):
            selected_values.append(grid[row][perm[row]])

        # 선택된 값들 중 최소값을 계산
        current_min_value = min(selected_values)

        # 그 중에서 최소값이 최대가 되는 값을 선택
        max_min_value = max(max_min_value, current_min_value)

    return max_min_value

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = find_max_min_value(grid, n)
print(result)