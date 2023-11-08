'''
해당 문제를 해결하기 위한 올바른 접근 방식은 모든 가능한 경로를 체크하는 것이며, 이를 위해 다음의 단계를 따라야 합니다:
1. 가능한 모든 첫 번째 점프 위치를 찾습니다. 이는 (1,1)부터 시작해야 하며, 다른 색상의 칸으로만 이동해야 합니다.
2. 각 첫 번째 점프 위치에 대해 가능한 두 번째 점프 위치를 찾습니다. 마찬가지로 이동한 칸은 이전 칸과 다른 색상이어야 합니다.
3. 두 번째 점프가 최종 목적지인 (R, C)로 이동하는지 확인합니다.
4. 두 점프를 통해 목적지에 도달하는 경우의 수를 세어 최종적으로 반환합니다.
'''

def count_jumps(R, C, board):
    # 가능한 점프 경로의 수를 저장할 변수
    count = 0
    
    # 가능한 모든 첫 번째 점프 위치 탐색
    for i in range(1, R):
        for j in range(1, C):
            # 첫 번째 점프가 유효한 색상 변경을 갖는 경우에만 계속
            if board[0][0] != board[i][j]:
                # 가능한 모든 두 번째 점프 위치를 탐색
                for x in range(i + 1, R):
                    for y in range(j + 1, C):
                        # 두 번째 점프가 유효한 색상 변경을 갖고, 목적지에 도달하는지 확인
                        if board[i][j] != board[x][y] and (x == R - 1 and y == C - 1):
                            count += 1

    return count

R, C = map(int, input().split())
board = [input().split() for _ in range(R)]

# 가능한 점프 경로의 수를 계산하고 출력
print(count_jumps(R, C, board))