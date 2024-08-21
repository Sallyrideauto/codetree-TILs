def count_tiling_ways(n):
    # Modulo constant
    MOD = 10007
    
    # dp[i] will hold the number of ways to tile a 2x(i) board
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # 1 way to fill a 2x0 board (doing nothing)
    if n >= 1:
        dp[1] = 1  # 1 way to fill a 2x1 board (just one 2x1 tile)
    
    if n >= 2:
        dp[2] = 3  # From the given example and description
    
    # Fill the dp array using the recurrence relation
    for i in range(3, n + 1):
        # dp[i - 2] can be filled in three ways: vertical 2x1, horizontal two 1x2, or one 2x2
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD
    
    return dp[n]

n = int(input())

print(count_tiling_ways(n))