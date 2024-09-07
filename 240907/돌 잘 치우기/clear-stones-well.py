from collections import deque
from itertools import combinations
import sys
input = sys.stdin.read

def bfs(grid, starts):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = deque(starts)
    for start in starts:
        visited.add(start)
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return len(visited)

def solve(n, k, m, grid, starts):
    rocks = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
    max_accessible = 0

    # 돌의 조합을 확인하고, 각 조합에 대해 BFS 실행
    for comb in combinations(rocks, m):
        # 선택된 돌들을 일시적으로 제거
        for (x, y) in comb:
            grid[x][y] = 0
        
        # BFS 실행하여 접근 가능한 칸 수 계산
        max_accessible = max(max_accessible, bfs(grid, starts))
        
        # 제거한 돌들을 복원
        for (x, y) in comb:
            grid[x][y] = 1
    
    return max_accessible

def main():
    # 입력 받기
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    m = int(data[2])
    
    grid = []
    index = 3
    for i in range(n):
        grid.append(list(map(int, data[index:index+n])))
        index += n
    
    starts = []
    for i in range(k):
        r, c = int(data[index])-1, int(data[index+1])-1
        starts.append((r, c))
        index += 2

    # 결과 출력
    print(solve(n, k, m, grid, starts))

if __name__ == "__main__":
    main()