def min_operations_to_one(N):
    # DP 테이블 초기화
    dp = [0] * (N + 1)

    # 2부터 N까지 순차적으로 최소 연산 횟수 계산
    for i in range(2, N + 1):
        # 1을 뺄 경우
        dp[i] = dp[i - 1] + 1
        
        # 2로 나누어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # 3으로 나누어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[N]

# 입력 받기
N = int(input())
print(min_operations_to_one(N))
