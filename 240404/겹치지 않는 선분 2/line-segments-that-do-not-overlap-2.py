def solution():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[1])

    cnt = 0
    end = lines[0][1]
    for i in range(1, n):
        if lines[i][0] > end:
            cnt += 1
            end = lines[i][1]

    print(cnt)

solution()