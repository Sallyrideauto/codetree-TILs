# 무한대를 나타내는 큰 수 설정
INF = float('inf')

# 플로이드-워셜 알고리즘
def floyd_warshall(graph):
    # 정점의 개수
    V = len(graph)

    # 최단 거리 테이블 초기화
    dist = [[INF] * V for _ in range(V)]
    
    # 그래프의 인접 행렬로 초기화
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    # 자기 자신으로 가는 경로는 0으로 설정
    for i in range(V):
        dist[i][i] = 0

    # 동적 계획법을 이용한 최단 경로 갱신
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# 예제 그래프
graph = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF], 
    [INF, INF, 1, 1, 0, 2], 
    [INF, INF, 5, INF, 2, 0]
]

# 플로이드-워셜 알고리즘 실행
distances = floyd_warshall(graph)

# 결과 출력
for row in distances:
    print(row)
