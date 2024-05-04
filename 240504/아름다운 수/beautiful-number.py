def count_beautiful_numbers(n):
    # 길이에 따른 아름다운 수의 개수를 저장할 DP 배열
    dp = [0] * (n + 1)

    # 초기값 설정
    if n >= 1:
        dp[1] = 1   # 예: 1
    if n >= 2:
        dp[2] = 2   # 예: 11, 22
    if n >= 3:
        dp[3] = 2   # 예: 111, 222
    if n >= 4:
        dp[4] = 1   # 예: 1111, 2222, 3333, 4444

    # DP 배열 채우기(길기 5부터 n까지)
    for i in range(5, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    return dp[n]

n = int(input())
print(count_beautiful_numbers(n))