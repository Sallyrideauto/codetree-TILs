N = int(input())
segments = []

for _ in range(N):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

# 두 선분이 겹치는지 확인하는 함수
def is_overlapping(seg1, seg2):
    x1, x2 = seg1
    y1, y2 = seg2
    return not (x2 < y1 or y2 < x1)

# 겹치지 않는 선분의 수를 세는 코드
non_overlapping_count = 1

for i in range(N):
    independent = True  # 초기 상태를 독립적인 선분이라고 가정
    for j in range(N):
        if i != j and is_overlapping(segments[i], segments[j]):
            independent = False  # 다른 선분과 겹치면 독립적이지 않음
            break
    if independent:
        non_overlapping_count += 1

print(non_overlapping_count)