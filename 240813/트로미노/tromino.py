import sys

board = [[0] * 200 for _ in range(200)]

def return_max1(x, y):
    # 첫 번째 블록에서의 최대값 반환
    max_sum = board[x][y] + board[x + 1][y] + board[x][y + 1] + board[x + 1][y + 1]
    answer = 0
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            now_sum = max_sum - board[i][j]
            answer = max(answer, now_sum)
    return answer

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])

    idx = 2
    for i in range(n):
        for j in range(m):
            board[i][j] = int(data[idx])
            idx += 1

    max_value = 0

    for i in range(n - 1):
        for j in range(m - 1):
            max_value = max(max_value, return_max1(i, j))

    for i in range(n):
        for j in range(m - 2):  # 1 * 3 모양
            max_value = max(max_value, board[i][j] + board[i][j + 1] + board[i][j + 2])

    for j in range(m):
        for i in range(n - 2):  # 3 * 1 모양
            max_value = max(max_value, board[i][j] + board[i + 1][j] + board[i + 2][j])

    print(max_value)

if __name__ == "__main__":
    main()