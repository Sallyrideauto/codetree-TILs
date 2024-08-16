def calculate_cost(k):
    # 주어진 k에 대한 마름모 형태의 격자 개수 계산
    return (k * k) + (k + 1) * (k + 1)

def get_gold_count(grid, n, k, x, y):
    # 주어진 중앙점 (x, y)에서 k에 따른 마름모 안의 금의 개수와 비용 계산
    gold_count = 0

    for i in range(n):
        for j in range(n):
            # 마름모의 조건을 확인
            if abs(x - i) + abs(y - j) <= k:
                gold_count += grid[i][j]

    return gold_count

def max_gold(n, m, grid):
    max_gold_count = 0

    # k의 범위를 0부터 n까지 반복
    for k in range(n + 1):
        for i in range(n):
            for j in range(n):
                gold_count = get_gold_count(grid, n, k, i, j)
                cost = calculate_cost(k)

                # 수익이 손해를 보지 않는지 확인
                total_value = gold_count * m
                if total_value >= cost:
                    max_gold_count = max(max_gold_count, gold_count)

    return max_gold_count

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = max_gold(n, m, grid)
print(result)