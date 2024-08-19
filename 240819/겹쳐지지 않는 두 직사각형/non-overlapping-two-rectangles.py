def calculate_rectangle_sum(matrix, x1, y1, x2, y2):
    # 주어진 좌표로 정의된 직사각형의 합을 계산
    total = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            total += matrix[i][j]
    return total

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    max_sum = float('-inf')

    # 모든 가능한 직사각형 조합 고려
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    # 첫 번째 직사각형의 합 계산
                    rect1_sum = calculate_rectangle_sum(matrix, x1, y1, x2, y2)

                    # 두 번째 직사각형 탐색
                    for x3 in range(n):
                        for y3 in range(m):
                            for x4 in range(x3, n):
                                for y4 in range(y3, m):
                                    # 두 직사각형이 겹치지 않는지 확인
                                    if not (x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1):
                                        continue

                                    # 두 번째 직사각형의 합 계산
                                    rect2_sum = calculate_rectangle_sum(matrix, x3, y3, x4, y4)

                                    # 총합을 계산하고 최대값 업데이트
                                    total_sum = rect1_sum + rect2_sum
                                    max_sum = max(max_sum, total_sum)

    print(max_sum)

if __name__ == "__main__":
    main()