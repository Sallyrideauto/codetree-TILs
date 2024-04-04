def solution():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[0])  # 시작점 값을 기준으로 선분들을 정렬합니다.

    cnt = 0  # cnt를 0으로 초기화합니다.
    end = lines[0][1]
    for i in range(1, n):
        if lines[i][0] > end:
            cnt += 1
            end = lines[i][1]

    print(cnt)

solution()