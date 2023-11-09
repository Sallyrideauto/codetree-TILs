'''
이 문제를 해결하기 위한 접근 방법은 각 선분의 시작점과 끝점을 정렬한 후, 겹치는 부분을 확인하는 것입니다. 
겹치지 않는 선분을 찾기 위해선 현재 선분의 끝점이 다음 선분의 시작점보다 작은 경우를 찾으면 됩니다.

프로그램은 다음과 같은 방식으로 작동합니다:
1. count_non_overlapping_segments 함수는 선분 리스트를 받아 처리합니다.
2. 선분들은 시작점 x1 기준으로 정렬됩니다.
3. non_overlapping_count 변수는 겹치지 않는 선분의 수를 추적합니다.
4. current_end 변수는 가장 최근에 확인된 선분의 끝점을 저장합니다.
5. 선분 리스트를 순회하면서, 각 선분의 시작점이 current_end보다 크면, 이 선분은 겹치지 않습니다.
6. 만약 겹치지 않는다면, non_overlapping_count를 증가시키고, current_end를 현재 선분의 끝점으로 업데이트합니다.
7. 마지막으로 겹치지 않는 선분의 총 수를 반환합니다.
'''

def count_non_overlapping_segments(segments):
    # 선분들을 시작점 기준으로 정렬
    sorted_segments = sorted(segments, key = lambda x: x[0])

    # 겹치지 않는 선분의 수 세기
    non_overlapping_count = 0
    current_end = -float('inf') # 현재 선분의 끝점 초기화

    # 정렬된 선분들 순회
    for segment in sorted_segments:
        # 현재 선분의 끝점이 다음 선분의 시작점보다 작다면, 겹치지 않음
        if segment[0] > current_end:
            non_overlapping_count += 1
            current_end = segment[1]

    # 겹치지 않는 선분의 수 반환
    return non_overlapping_count

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

print(count_non_overlapping_segments(segments))