def shortest_common_supersequence_length(s, t):
    # 두 문자열의 길이를 구합니다.
    n = len(s)
    m = len(t)

    # dp 테이블 초기화
    # dp[i][j]는 s[0:i]와 t[0:j]의 LCS 길이를 저장합니다.
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 동적 계획법으로 LCS 길이 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:  # 문자가 같을 때
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 문자가 다를 때
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이를 가져옵니다.
    lcs_length = dp[n][m]

    # 최소 공통 상위수열의 길이를 계산
    scs_length = n + m - lcs_length

    return scs_length

# 입력 받기
s = input().strip()
t = input().strip()

# 결과 출력
print(shortest_common_supersequence_length(s, t))
