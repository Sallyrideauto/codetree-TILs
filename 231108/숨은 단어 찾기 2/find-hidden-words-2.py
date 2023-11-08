# 입력 받기
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# LEE를 찾는 함수 정의
def search_LEE(x, y, dx, dy):
    for i in range(3):
        # 새로운 탐색 위치
        new_x, new_y = x + dx * i, y + dy * i
        # 그리드 범위를 벗어나면 바로 False 반환
        if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M:
            return False
        # 그리드 범위 내에 있지만 LEE 문자열과 매치되지 않으면 False 반환
        if grid[new_x][new_y] != 'LEE'[i]:
            return False
    # 모든 검사를 통과하면 True 반환
    return True

# 모든 위치에 대해 8가지 방향 탐색
count = 0
for i in range(N):
    for j in range(M):
        # 방향 벡터 : 상, 하, 좌, 우, 대각선 4방향
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            if search_LEE(i, j, dx, dy):
                count += 1

print(count)