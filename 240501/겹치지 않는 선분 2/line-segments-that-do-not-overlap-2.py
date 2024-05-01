from itertools import combinations

# 두 선분이 겹치지 않는지 확인하는 함수
def is_intersecting(p1, q1, p2, q2):
    # 두 점이 주어졌을 때, 세 번째 점이 선분 위에 있는지 확인하는 함수
    def on_segment(p, q, r):
        return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

    # 세 점의 방향성을 결정하는 함수
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # collinear
        elif val > 0:
            return 1  # clockwise
        else:
            return -1  # counter-clockwise
    
    # 방향성을 통해 교차 여부를 확인
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    # 일반적인 교차 조건
    if o1 != o2 and o3 != o4:
        return True
    # 특수한 경우: 콜리니어하고 선분 위에 있는 경우
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    return False

# 선분들이 겹치지 않는지 확인하는 함수
def is_disjoint(segments):
    for s1, s2 in combinations(segments, 2):
        if is_intersecting(s1[0], s1[1], s2[0], s2[1]):
            return False
    return True

# 최대 겹치지 않는 선분 집합을 찾는 함수
def max_non_overlapping_segments(segments):
    n = len(segments)
    max_count = 0
    
    # 모든 조합을 생성
    for r in range(1, n + 1):
        all_combinations = combinations(segments, r)
        for combination in all_combinations:
            if is_disjoint(combination):
                max_count = max(max_count, len(combination))
    
    return max_count

# 입력 받기
n = int(input())
segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append(((x1, 0), (x2, 1)))

# 결과 출력
print(max_non_overlapping_segments(segments))