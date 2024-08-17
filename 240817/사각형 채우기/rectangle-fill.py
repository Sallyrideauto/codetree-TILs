def count_ways(n):
    # 모듈로 연산을 위한 상수
    MOD = 10007

    # dp 배열 초기화
    dp = [0] * (n + 1)

    # 기본 사례
    dp[0] = 1   # 2 * 0 크기의 사각형은 1가지 방법(비어 있는 경우)
    dp[1] = 1   # 2 * 1 크기의 사각형은 1가지 방법(세로로 놓기)

    # dp 배열을 채우는 과정
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

n = int(input())

result = count_ways(n)
print(result)