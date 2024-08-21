n = int(input())

dp = [0] * 1001
dphalf = [0] * 1001 # 마지막 1개가 한 칸만 채워진 경우

dp[1] = 2
dp[2] = 7

dphalf[1] = 1
dphalf[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] + dphalf[i - 1] * 2) % 1000000007
    dphalf[i] = (dp[i - 1] + dphalf[i - 1]) % 1000000007

print(dp[n])