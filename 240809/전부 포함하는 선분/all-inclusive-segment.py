def find_min_length_to_cover_all_segments(n, segments):
    # 전체 범위를 포함할 수 있는 선분을 찾기
    def range_cover(segments):
        start = min(seg[0] for seg in segments)
        end = max(seg[1] for seg in segments)
        return end - start

    # 전체 범위를 포함할 수 있는 선분의 길이
    min_length = range_cover(segments)
    
    for i in range(n):
        # 선분 i를 제거한 후 나머지 선분들로 범위를 계산
        remaining_segments = segments[:i] + segments[i+1:]
        length_with_removed = range_cover(remaining_segments)
        min_length = min(min_length, length_with_removed)
    
    return min_length

# 입력 읽기
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
segments = [(int(data[2*i+1]), int(data[2*i+2])) for i in range(n)]

# 최소 길이 계산
result = find_min_length_to_cover_all_segments(n, segments)
print(result)