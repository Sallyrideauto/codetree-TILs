def solution():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[0])  # 시작점을 기준으로 선분을 정렬합니다.

    cnt = 0
    end = -1
    for line in lines:
        if line[0] > end:
            cnt += 1
            end = line[1]

    print(cnt)

solution()