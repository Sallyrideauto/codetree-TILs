n, m = map(int, input().split())

# 그래프 초기화(인접 리스트 사용)
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

vertex_cnt = 0

# 그래프에 간선 추가
for _ in range(m):
    start_point, end_point = map(int, input().split())
    graph[start_point].append(end_point)
    graph[end_point].append(start_point)

def dfs(vertex):
    global vertex_cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)

visited[1] = True
dfs(1)

print(vertex_cnt)