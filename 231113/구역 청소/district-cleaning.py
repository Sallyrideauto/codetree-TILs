a, b = map(int, input().split())
c, d = map(int, input().split())

# 겹치는 구간의 시작점은 두 구간의 시작점 중 더 큰 값
overlap_start = max(a, c)
# 겹치는 구간의 끝점은 두 구간의 끝점 중 더 작은 값
overlap_end = min(b, d)

# 청소된 영역 계산
# 겹치지 않는 A의 부분 + 겹치지 않는 B의 부분 + 겹치는 부분
cleaned_area = (b - a + 1) + (d - c + 1) - max(0, (overlap_end - overlap_start + 1))

print(cleaned_area - 1)