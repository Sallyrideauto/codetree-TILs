def solution():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[0])  # 시작점을 기준으로 선분을 정렬합니다.

    cnt = 0  # 처음에는 겹치지 않는 선분이 하나라도 존재하므로 cnt를 1로 초기화합니다.
    end = lines[0][1]  # 초기 end 값을 첫 번째 선분의 끝점으로 설정합니다.
    for line in lines[1:]:
        if line[0] > end:  # 현재 선분의 시작점이 이전 선분의 끝점보다 크다면 겹치지 않는 선분이므로 cnt를 증가시킵니다.
            cnt += 1
            end = line[1]  # 현재 선분의 끝점을 end로 업데이트합니다.

    print(cnt)

solution()