def tsp(n, cost):
    # dp[visited][i]는 방문한 정점 집합과 현재 정점이 i일 때의 최소 비용을 저장
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    
    # 출발점에서 시작할 때의 비용은 0
    dp[1][0] = 0
    
    # 비트마스킹을 통해 모든 상태를 처리
    for visited in range(1 << n):
        for i in range(n):
            if visited & (1 << i):
                for j in range(n):
                    if not visited & (1 << j) and cost[i][j] > 0:
                        next_visited = visited | (1 << j)
                        dp[next_visited][j] = min(dp[next_visited][j], dp[visited][i] + cost[i][j])
    
    # 모든 정점을 방문한 상태에서 출발점으로 돌아가는 최소 비용을 계산
    answer = INF
    for i in range(1, n):
        if cost[i][0] > 0:
            answer = min(answer, dp[(1 << n) - 1][i] + cost[i][0])
    
    return answer

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
cost = []
index = 1
for i in range(n):
    cost.append([int(data[index + j]) for j in range(n)])
    index += n

# 결과 출력
print(tsp(n, cost))