from collections import deque

def find_shortest_path(n, m, grid):
    # 방향 벡터 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 여부를 기록할 2차원 리스트
    visited = [[False] * m for _ in range(n)]
    
    # BFS를 위한 큐 초기화 (시작점: (0, 0), 초기 거리: 1)
    queue = deque([(0, 0)])
    visited[0][0] = True  # 시작점 방문 처리
    
    # 거리 배열 초기화
    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 0  # 시작점 거리 설정
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치가 우측 하단일 경우 최단 거리 반환
        if x == n - 1 and y == m - 1:
            return distance[x][y]
        
        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 이동 가능한 좌표인지 확인 (범위 내, 뱀 없는 칸, 방문하지 않은 칸)
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1  # 이전 거리에서 1 추가
                queue.append((nx, ny))
    
    # 모든 경로 탐색 후 도달 불가능할 경우
    return -1

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 최단 거리 계산 및 출력
result = find_shortest_path(n, m, grid)
print(result)