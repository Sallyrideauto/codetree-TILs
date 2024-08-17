def max_k_by_k_sum(n, k, grid):
    # Prefix sum 배열 초기화
    prefix_sum = [[0] * n for _ in range(n)]

    # Prefix sum 계산
    for i in range(n):
        for j in range(n):
            prefix_sum[i][j] = grid[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    # 최대 k * k 합 계산
    max_sum = float('-inf')

    for i in range(k - 1, n):
        for j in range(k - 1, n):
            r1, c1 = i - k + 1, j - k + 1
            r2, c2 = i, j
            current_sum = prefix_sum[r2][c2]
            if r1 > 0:
                current_sum -= prefix_sum[r1 - 1][c2]
            if c1 > 0:
                current_sum -= prefix_sum[r2][c1 - 1]
            if r1 > 0 and c1 > 0:
                current_sum += prefix_sum[r1 - 1][c1 - 1]
            max_sum = max(max_sum, current_sum)

    return max_sum

n, k = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

print(max_k_by_k_sum(n, k, grid))