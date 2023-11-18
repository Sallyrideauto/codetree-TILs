'''
1. 선분들을 시작점 순으로 정렬합니다.
2. 각 선분을 순회하면서 해당 선분을 제외하고 나머지 선분들의 겹치는 범위를 찾습니다.
3. 나머지 선분들 중 겹치는 범위가 없다면, 다음 선분을 제외하고 다시 검사합니다.
4. 모든 나머지 선분들이 겹치는 범위를 가지면 “Yes”를 반환합니다.
5. 모든 선분을 제외해 봤을 때 겹치는 범위를 찾지 못하면 “No”를 반환합니다.
'''

def can_overlap_after_removing_one(segments):
    # 모든 선분을 시작점과 끝점으로 정렬
    segments.sort(key = lambda x: (x[0], x[1]))

    # 각 선분을 제거 해 보면서 나머지 선분들이 겹치는지 확인
    for i in range(len(segments)):
        # 현재 선분을 제외한 나머지 선분들을 선택
        temp_segments = segments[:i] + segments[i + 1:]

        # 선택된 선분들의 겹치는 범위 탐색
        overlap_start, overlap_end = temp_segments[0]
        for start, end in temp_segments[1:]:
            overlap_start = max(overlap_start, start)
            overlap_end = min(overlap_end, end)
            # 겹치는 범위가 유효하지 않으면 다음 선분으로 넘어가기
            if overlap_start > overlap_end:
                break
        else:
            # 모든 선택된 선분이 겹치면 "Yes"를 반환
            return "Yes"

    # 모든 시도에서 겹치는 선분을 찾지 못하면 "No"를 반환
    return "No"

n = int(input())

segments_info = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments_info.append((x1, x2))

print(can_overlap_after_removing_one(segments_info))