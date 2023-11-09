'''
이 문제는 모든 가능한 1x3 격자 조합을 탐색하여 최대 동전 수를 찾는 문제입니다. 
겹치지 않게 격자를 잡아야 하므로, 한 격자를 고정한 후 나머지 격자에 대해 모든 가능한 위치를 탐색해야 합니다.
'''

def max_coins(N, grid):
    # 최대 동전 개수를 저장할 변수 초기화
    max_coins = 0

    # 격자 내 모든 위치에 대해 1*3 격자를 위치시키고 탐색
    for i in range(N):
        for j in range(N - 2):  # 1*3 격자를 놓을 수 있는 열의 시작점
            # 첫 번째 1*3 격자에 포함된 동전 수를 계산
            first = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]

            # 나머지 위치에 두 번째 1*3 격자를 놓는 모든 경우를 탐색
            for x in range(N):
                for y in range(N - 2):
                    # 겹치는 부분을 배제
                    if x == i and (y in range(j - 2, j + 3)):
                        continue
                    
                    # 두 번째 1*3 격자에 포함된 동전 수를 계산
                    second = grid[x][y] + grid[x][y + 1] + grid[x][y + 2]

                    # 최대 동전 수를 갱신
                    max_coins = max(max_coins, first + second)
    
    return max_coins

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

print(max_coins(N, grid))