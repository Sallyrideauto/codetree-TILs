def is_non_overlapping(selected_segments):
    # 선분이 서로 겹치는지 여부를 확인하는 함수
    for i in range(len(selected_segments)):
        for j in range(i + 1, len(selected_segments)):
            x1, x2 = selected_segments[i]
            y1, y2 = selected_segments[j]
            if not (x2 < y1 or y2 < x1):    # 겹치는 경우
                return False
    return True

def find_max_segments(segments, idx = 0, selected = []):
    # 현재까지 선택된 선분 중 겹치지 않는 최대 수를 찾는 재귀 함수
    if idx == len(segments):
        if is_non_overlapping(selected):
            return len(selected)
        else:
            return 0 

    # 현재 선분을 선택하지 않는 경우
    option1 = find_max_segments(segments, idx + 1, selected)

    # 현재 선분을 선택하는 경우
    selected.append(segments[idx])
    option2 = find_max_segments(segments, idx + 1, selected)
    selected.pop()

    return max(option1, option2)

n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

# 겹치지 않게 고를 수 있는 최대 선분의 수 탐색
result = find_max_segments(segments)
print(result)