def max_positive_rectangle(matrix, n, m):
    max_area = -1

    # 모든 가능한 직사각형의 좌표 탐색
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    # 현재 직사각형이 양수인지 확인
                    valid_rectangle = True
                    for i in range(x1, x2 + 1):
                        for j in range(y1, y2 + 1):
                            if matrix[i][j] <= 0:   # 양수가 아닌 경우
                                valid_rectangle = False
                                break
                            if not valid_rectangle:
                                break

                    # 유효한 직사각형인 경우 면적 계산
                    if valid_rectangle:
                        area = (x2 - x1 + 1) * (y2 - y1 + 1)
                        max_area = max(max_area, area)

    return max_area

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]

    result = max_positive_rectangle(matrix, n, m)

    print(result)

if __name__ == "__main__":
    main()