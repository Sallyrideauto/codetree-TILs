def max_alternating_groups(n, numbers):
    # 각 숫자의 누적 합을 계산하여 사용
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + numbers[i - 1]

    # dp[i][0]는 i까지 고려하여 마지막 그룹이 짝수인 최대 그룹 수
    # dp[i][1]는 i까지 고려하여 마지막 그룹이 홀수인 최대 그룹 수
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            group_sum = prefix_sums[i] - prefix_sums[j]
            if group_sum % 2 == 0:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)  # 현재 짝수 그룹이면 이전에 홀수 그룹이어야 함
            else:
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)  # 현재 홀수 그룹이면 이전에 짝수 그룹이어야 함

    # 최대 그룹 수를 찾음
    return max(dp[n][0], dp[n][1])

# 사용자 입력
N = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(max_alternating_groups(N, numbers))