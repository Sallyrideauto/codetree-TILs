n = int(input())
blocks = []

for _ in range(n):
    block_n = int(input())
    blocks.append(block_n)

s1, e1 = map(int, input().split())  # 첫 번째 제거 범위
s2, e2 = map(int, input().split())  # 두 번째 제거 범위

# 첫 번째 범위 제거
del blocks[s1 - 1:e1]   # 파이썬의 인덱스는 0부터 시작하므로 1을 빼 줌

# 두 번째 제거 범위를 조정(블록이 줄었으므로 인덱스도 변경됨)
s2_adjusted = max(1, s2 - (e1 - s1 + 1))
e2_adjusted = max(s2_adjusted, e2 - (e1 - s1 + 1))

# 남은 블록의 수를 기반으로 범위 조정
s2_final = s2_adjusted - 1
e2_final = min(len(blocks), e2_adjusted - 1)

# 두 번째 범위 제거, 범위가 유효하다면
if s2_final < len(blocks):
    del blocks[s2_final:e2_final + 1]

# 결과 출력
print(len(blocks))
for block in blocks:
    print(block)