'''
주어진 선분들 중 겹치지 않는 것을 찾기 위해서는, 다음과 같은 접근 방법을 사용할 수 있습니다:
1. 선분의 끝점을 기준으로 오름차순 정렬합니다. (끝점이 같다면 시작점이 더 작은 것부터 정렬)
2. 첫 번째 선분을 겹치지 않는 선분으로 선택하고, 선택한 선분의 끝점을 저장합니다.
3. 다음 선분부터 검사하여, 현재 저장된 끝점보다 시작점이 크거나 같은 선분을 찾습니다.
   이 경우에만 겹치지 않는 선분으로 판단하고, 선택한 선분의 끝점을 업데이트합니다.
4. 모든 선분을 검사할 때까지 반복합니다.
'''

def count_non_overlapping_segments(segments):
    # 겹치지 않는 선분의 수를 저장할 변수 초기화
    non_overlapping_count = 0

    # 각 선분을 기준으로 다른 선분들과 겹치는지 확인
    for i in range(N):
        overlap = False
        for j in range(N):
            if i != j:
                # i번째 선분의 끝점이 j번째 선분의 시작점보다 클 경우, 겹친다고 판단
                if segments[i][1] > segments[j][0]:
                    overlap = True
                    break
        # 만약 겹치는 선분이 없다면 카운트를 증가
        if not overlap:
            non_overlapping_count += 1

    # 겹치지 않는 선분의 수 반환
    return non_overlapping_count

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

print(count_non_overlapping_segments(segments))