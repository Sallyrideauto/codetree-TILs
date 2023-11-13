# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# 겹치는 조건 확인
if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
    print("nonoverlapping")
else:
    print("overlapping")