def count_ways(n):
    MOD = 10007

    # dp 배열 초기화
    dp = [0] * (n + 1)

    # 초기 조건 설정
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 1

    # dp 배열을 채워 나가기
    for i in range(4, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 3]) % MOD

    return dp[n]

n = int(input())
print(count_ways(n))