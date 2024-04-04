def solution(n, m, board):
    # dp 배열을 모두 0으로 초기화합니다.
    dp = [[0] * m for _ in range(n)]
    
    # 첫 번째 행은 그대로 복사합니다.
    dp[0] = board[0]
    
    # 두 번째 행부터는 이전 행까지의 최대 부분합을 고려하여 현재 위치까지의 최대 부분합을 계산합니다.
    for i in range(1, n):
        for j in range(m):
            # 왼쪽 위, 위, 오른쪽 위에서의 최대 부분합을 찾습니다.
            max_sum = max(dp[i-1][max(j-1, 0):min(j+2, m-1)])
            # 현재 위치까지의 최대 부분합은 현재 값과 이전 행의 최대 부분합을 더한 값 중 큰 것입니다.
            dp[i][j] = max_sum + board[i][j]
    
    # 마지막 행의 최대 부분합 중 최대값을 반환합니다.
    return max(dp[-1])

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, board))

if __name__ == "__main__":
    main()