MOD = 1000000007

def tiling_ways(n):
    if n == 1:
        return 2
    elif n == 2:
        return 7

    # dp 배열 초기화
    dp = [0] * (n + 1)
    
    # 초기 값 설정
    dp[1] = 2
    dp[2] = 7
    dp[3] = 22
    
    # DP 점화식을 통한 값 채우기
    for i in range(4, n + 1):
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2]) % MOD
    
    return dp[n]

# 입력 받기
n = int(input())

# 출력
print(tiling_ways(n))