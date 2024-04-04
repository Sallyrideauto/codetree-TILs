def solution():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort()  # 선분을 시작점과 끝점을 동시에 고려하여 정렬합니다.

    cnt = 0
    end = 0
    for line in lines:
        if line[0] > end:
            cnt += 1
            end = line[1]

    print(cnt)

solution()