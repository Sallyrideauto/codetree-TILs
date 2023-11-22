def max_moves_to_consecutive(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 간격 계산
    left_gap = positions[1] - positions[0]
    right_gap = positions[2] - positions[1]

    # 최대 이동 횟수 계산
    return max(left_gap, right_gap) - 1

a, b, c = map(int, input().split())
print(max_moves_to_consecutive(a, b, c))