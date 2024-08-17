def count_ways(n):
    # 모듈로 연산을 위한 상수
    MOD = 1000000007

    # dp 배열 초기화
    dp = [0] * (n + 1)
    
    # 기본 사례
    dp[0] = 1  # 2 × 0 크기의 사각형은 1가지 방법 (비어있는 경우)
    
    if n >= 1:
        dp[1] = 2  # 2 × 1 크기의 사각형은 2가지 방법 (세로로 놓기, 가로로 놓기)
    if n >= 2:
        dp[2] = 7  # 2 × 2 크기의 사각형은 7가지 방법

    # dp 배열을 채우는 과정
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2 + dp[i - 3]) % MOD

    return dp[n]

# 입력 받기
n = int(input())

# 결과 출력
result = count_ways(n)
print(result)