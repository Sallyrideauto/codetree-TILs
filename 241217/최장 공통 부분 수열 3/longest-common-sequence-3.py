# 두 배열의 최장 공통 부분 수열(LCS)을 찾는 프로그램입니다.
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp 테이블 생성
dp = [[0] * (m + 1) for _ in range(n + 1)]

# dp 테이블 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:  # 현재 문자가 같을 때
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 같지 않을 때
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 추적
lcs = []
i, j = n, m
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        lcs.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

# 최장 공통 부분 수열 출력
lcs.reverse()
print(' '.join(map(str, lcs)))
