from collections import deque

# 나이트의 이동 문제를 해결하기 위한 BFS 함수
def knight_minimum_moves(n, start, end):
    # 나이트의 8가지 이동 방향 정의 (dy, dx)
    moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]

    # 방문 여부를 기록하는 배열
    visited = [[False] * n for _ in range(n)]

    # BFS 초기화
    queue = deque([(start[0], start[1], 0)])  # (현재 y, 현재 x, 이동 횟수)
    visited[start[0]][start[1]] = True

    while queue:
        y, x, steps = queue.popleft()

        # 도착 지점에 도달한 경우
        if (y, x) == end:
            return steps

        # 8가지 방향으로 나이트 이동
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, steps + 1))

    # 도달할 수 없는 경우
    return -1

# 입력 처리
n = int(input())  # 격자 크기
r1, c1, r2, c2 = map(int, input().split())  # 시작 위치와 끝 위치
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1  # 1-based index를 0-based index로 변환

# 결과 출력
result = knight_minimum_moves(n, (r1, c1), (r2, c2))
print(result)
