N, M = map(int, input().split())
knapsack_arr = []

for _ in range(N):
    w, v = map(int, input().split())
    # 무게 대비 가치를 계산하여 (w, v, v/w) 형태로 리스트에 추가
    knapsack_arr.append((w, v, v/w))

# 무게 대비 가치가 높은 순서로 보석들을 정렬
knapsack_arr.sort(key=lambda x: x[2], reverse=True)

# 최대 가치를 계산하기 위한 변수
max_value = 0.0
remaining_capacity = M

# 그리디 알고리즘 적용
for w, v, ratio in knapsack_arr:
    if remaining_capacity >= w:
        # 가방에 전부 보석을 담을 수 있는 경우
        max_value += v
        remaining_capacity -= w
    else:
        # 보석의 일부만 담을 수 있는 경우
        max_value += v * (remaining_capacity / w)
        break

print(f"{max_value:.3f}")