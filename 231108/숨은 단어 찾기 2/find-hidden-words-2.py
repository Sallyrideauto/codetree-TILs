# 입력 받기
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# LEE를 찾는 함수 정의
def search_LEE(x, y, dx, dy):
    try:
        # 주어진 방향으로 LEE가 나오는지 확인
        for i in range(3):
            if grid[x + dx * i][y + dy * i] != 'LEE'[i]:
                return False
        return True
    except IndexError:
        # 인덱스 에러가 발생하면 범위 밖이므로 False 반환
        return False

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