from collections import deque

def bfs(grid, visited, n, start_x, start_y):
    # BFS 초기화
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    num = grid[start_x][start_y]
    
    block_size = 0
    while queue:
        x, y = queue.popleft()
        block_size += 1  # 블럭 크기 증가
        
        # 상하좌우 인접한 칸 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            # 범위와 같은 숫자 체크
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == num:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return block_size

def main():
    n = int(input())  # 격자 크기 입력
    grid = [list(map(int, input().split())) for _ in range(n)]  # 격자 입력
    visited = [[False] * n for _ in range(n)]  # 방문 배열 초기화

    total_blocks = 0
    max_block_size = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:  # 방문하지 않은 셀인 경우
                block_size = bfs(grid, visited, n, i, j)  # BFS 실행
                if block_size >= 4:  # 블럭 크기가 4 이상일 경우
                    total_blocks += 1  # 터지는 블럭 수 증가
                max_block_size = max(max_block_size, block_size)  # 최대 블럭 크기 업데이트

    print(total_blocks, max_block_size)  # 결과 출력

if __name__ == "__main__":
    main()