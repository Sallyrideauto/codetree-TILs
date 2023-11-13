# 입력 받기
a, b = map(int, input().split())
c, d = map(int, input().split())

# 겹치는 구간의 시작과 끝을 계산합니다.
overlap_start = max(a, c)
overlap_end = min(b, d)

# 겹치는 구간의 길이를 계산합니다. 겹치는 구간이 없으면 0입니다.
overlap_length = max(0, overlap_end - overlap_start + 1)

# 전체 청소된 구역의 길이는 두 구역의 길이의 합에서 겹치는 구간의 길이를 뺀 것입니다.
cleaned_length = (b - a + 1) + (d - c + 1) - overlap_length

print(cleaned_length - 1)