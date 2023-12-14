def min_enclosing_line_segment_length(segments):
    # 선분들을 시작점(x1) 기준으로 정렬
    segments.sort()

    # 가장 긴 선분을 찾기 위해 각 선분의 길이를 계산
    segment_lengths = [x2 - x1 for x1, x2 in segments]

    # 가장 긴 선분의 길이와 인덱스를 찾음
    max_length = max(segment_lengths)
    max_length_index = segment_lengths.index(max_length)

    # 가장 긴 선분을 제외하고 나머지 선분들을 포함하는 선분의 길이를 계산
    if max_length_index == 0:
        # 가장 긴 선분이 리스트의 처음에 있다면, 마지막 선분의 끝점에서 두 번째 선분의 시작점을 뺀다.
        return segments[-1][1] - segments[1][0]
    elif max_length_index == len(segments) - 1:
        # 가장 긴 선분이 리스트의 마지막에 있다면, 끝에서 두 번째 선분의 끝점에서 첫 번째 선분의 시작점을 뺀다.
        return segments[-2][1] - segments[0][0]
    else:
        # 그렇지 않다면, 가장 긴 선분을 제외한 나머지 선분들 중 첫 번째 선분의 시작점과 마지막 선분의 끝점 사이의 거리를 구한다.
        return max(segments[-1][1] - segments[0][0] - max_length,
                   segments[max_length_index][1] - segments[0][0],
                   segments[-1][1] - segments[max_length_index + 1][0])


n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

# 선분의 최소 길이 계산 및 출력
print(min_enclosing_line_segment_length(segments))