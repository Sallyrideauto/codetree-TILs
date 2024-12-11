def calculate_remaining_y_sum(points):
    # 딕셔너리를 이용해 x좌표별 최소 y값을 저장
    x_to_min_y = {}

    for x, y in points:
        if x in x_to_min_y:
            # 동일한 x좌표가 이미 존재하면 더 작은 y값으로 업데이트
            x_to_min_y[x] = min(x_to_min_y[x], y)
        else:
            # 처음 등장하는 x좌표라면 추가
            x_to_min_y[x] = y

    # 남아있는 점들의 y값을 합산
    total_y_sum = sum(x_to_min_y.values())
    return total_y_sum

# 입력 받기
n = int(input())  # 점의 개수
points = []  # 점들의 리스트

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 결과 계산
result = calculate_remaining_y_sum(points)
print(result)
