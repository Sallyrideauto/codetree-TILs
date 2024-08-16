def fibbo(n, memo):
    if memo[n] != -1:        # 이미 n번째 값을 구해본 적이 있다면
        return memo[n]       # memo에 적혀있는 값을 반환
    if n <= 2:               # n이 2 이하인 경우에는 종료 조건
        memo[n] = 1          # n이 1이나 2일 때 피보나치 수는 1
    else:                    # n이 3 이상인 경우
        memo[n] = fibbo(n - 1, memo) + fibbo(n - 2, memo)  # 점화식을 이용하여 답을 구한 뒤 해당 값을 memo에 저장
    return memo[n]                             # memo 값을 반환

n = int(input())
memo = [-1] * (n + 1)   # memo 리스트 초기화(n + 1 크기의 리스트, 모든 값은 -1로 설정)

print(fibbo(n, memo))