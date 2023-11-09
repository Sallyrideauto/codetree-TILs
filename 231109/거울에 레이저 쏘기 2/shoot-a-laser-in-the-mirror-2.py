'''
이 문제는 격자에서의 레이저 반사를 시뮬레이션하는 것을 요구합니다. 
각 거울은 레이저를 90도로 반사시키는데, 거울의 종류에 따라 반사의 방향이 달라집니다.

이 코드는 다음 단계로 문제를 해결합니다:
1. simulate_lasers 함수 내에서 시작 위치와 방향을 계산합니다.
2. 격자를 벗어날 때까지 레이저가 이동하는 경로를 따라가며, 거울에 튕기는 횟수를 계산합니다.
3. / 거울과 \ 거울에 따라 반사되는 방향이 다르므로, 각 경우에 따라 새로운 방향을 정합니다.
4. 방향에 따라 다음 위치로 레이저를 이동시킵니다.
5. 최종적으로 거울에 튕기는 횟수를 반환합니다.
'''

def simulate_lasers(N, grid, K):
    # 격자의 각 변에 대응하는 레이저의 시작 위치를 정의합니다.
    # 위쪽 변을 1부터 시작하여 시계 방향으로 번호를 매깁니다.
    def get_start_position(K):
        if K <= N:
            return (0, K-1, 'D')
        elif K <= 2*N:
            return (K-N-1, N-1, 'L')
        elif K <= 3*N:
            return (N-1, 3*N-K, 'U')
        else:
            return (4*N-K, 0, 'R')

    # 레이저가 격자를 벗어났는지 확인합니다.
    def is_out_of_bounds(x, y):
        return x < 0 or y < 0 or x >= N or y >= N

    # 초기 위치와 방향을 설정합니다.
    x, y, direction = get_start_position(K)
    bounces = 0

    # 레이저가 격자 안에 있을 때까지 반복합니다.
    while not is_out_of_bounds(x, y):
        # 거울의 타입에 따라 방향을 바꿉니다.
        if grid[x][y] == '/':
            direction = {'U': 'R', 'R': 'U', 'D': 'L', 'L': 'D'}[direction]
        else: # grid[x][y] == '\\'
            direction = {'U': 'L', 'L': 'U', 'D': 'R', 'R': 'D'}[direction]
        bounces += 1

        # 새 방향으로 레이저를 이동시킵니다.
        if direction == 'U':
            x -= 1
        elif direction == 'D':
            x += 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1

    return bounces

# 입력 받기
N = int(input())
grid = [input() for _ in range(N)]
K = int(input())

# 레이저 시뮬레이션 실행 및 출력
print(simulate_lasers(N, grid, K))