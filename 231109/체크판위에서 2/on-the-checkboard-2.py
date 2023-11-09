'''
이 문제는 가능한 모든 점프 경로를 탐색하여 규칙에 부합하는 경우의 수를 찾는 것입니다.

이 코드는 다음과 같이 작동합니다:
1. 가능한 모든 점프의 시작 위치를 찾습니다. 
   시작 위치는 도착 위치(맨 오른쪽 하단)와 색깔이 달라야 하며, 맨 왼쪽 상단에서 시작해야 합니다.
2. 두 점프 지점(start_jump, end_jump)이 유효한지 검사합니다. 
   첫 번째 점프가 두 번째 점프보다 먼저 일어나야 하며, 두 점프 지점의 색이 서로 달라야 합니다.
3. 시작점과 중간 점프 지점의 색이 다르고, 중간 점프 지점과 도착점의 색도 달라야 합니다.
4. 유효한 경로를 찾을 때마다 카운트를 증가시킵니다.

코드의 시간 복잡도는 O(R^2 * C^2) 입니다. 
입력이 주어진 제한 내에서는 문제가 없으나, R과 C가 매우 큰 경우에는 최적화가 필요할 수 있습니다.
'''

def count_paths(R, C, grid):
    # 가능한 점프 시작 위치를 저장할 리스트입니다.
    valid_jumps = []

    # 모든 칸을 순회하며 유효한 점프가 가능한 위치를 찾습니다.
    for i in range(R-1):
        for j in range(C-1):
            if grid[i][j] != grid[R-1][C-1]:  # 시작점과 도착점의 색이 다른 경우만 탐색합니다.
                valid_jumps.append((i, j))

    path_count = 0

    # 유효한 점프 위치 각각에 대해 가능한 점프를 탐색합니다.
    for start_jump in valid_jumps:
        for end_jump in valid_jumps:
            if start_jump < end_jump:  # 시작 점프가 종료 점프보다 왼쪽 상단에 있어야 합니다.
                if grid[start_jump[0]][start_jump[1]] != grid[end_jump[0]][end_jump[1]]:
                    # 중간 점프 지점의 색이 시작점과 다른 경우에만 카운트합니다.
                    if grid[0][0] != grid[start_jump[0]][start_jump[1]] and grid[start_jump[0]][start_jump[1]] != grid[R-1][C-1]:
                        path_count += 1

    return path_count

# 입력 받기
R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

# 이동 경로 수 계산 및 출력
print(count_paths(R, C, grid))