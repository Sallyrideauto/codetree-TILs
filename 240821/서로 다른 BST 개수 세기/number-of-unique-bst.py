def num_trees(N):
    # N이 0 또는 1일 경우, 만들 수 있는 BST는 1개 뿐
    if N == 0 or N == 1:
        return 1
    
    # dp 테이블 초기화(0부터 N까지 저장할 수 있도록 크기 N + 1로 설정)
    dp = [0] * (N + 1)

    # dp[0]과 dp[1]은 1로 초기화
    dp[0], dp[1] = 1, 1

    # 2부터 N까지 차례대로 dp 값을 채워 나감
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    # 결과적으로 우리가 구하는 값은 dp[N]
    return dp[N]

N = int(input())

print(num_trees(N))