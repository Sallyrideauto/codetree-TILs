def solution(n, m, board):
    # dp[i][j]는 (i, j) 위치까지의 최대 합을 저장합니다.
    dp = [[0] * m for _ in range(n)]
    
    # 첫 번째 행은 바로 이전 행의 값을 더합니다.
    for j in range(m):
        dp[0][j] = board[0][j]
    
    # 각 위치까지의 최대 합을 구합니다.
    for i in range(1, n):
        for j in range(m):
            # 이전 행의 최대 합 중 현재 열을 포함한 부분합의 최대값을 선택합니다.
            dp[i][j] = max(dp[i-1][max(j-1, 0):min(j+2, m-1)]) + board[i][j]
    
    # 전체 영역에서의 최대 합을 반환합니다.
    return max(max(row) for row in dp)

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, board))

if __name__ == "__main__":
    main()