def continuous_nums(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 왼쪽과 중간, 오른쪽과 중간 사이의 간격을 계산
    left_gap = positions[1] - positions[0]
    right_gap = positions[2] - positions[1]

    # 두 간격 중 하나가 1이면, 다른 한쪽만 이동하면 됨
    if left_gap == 1 or right_gap == 1:
        return min(left_gap, right_gap)

    # 두 간격 모두 1보다 크면, 두 사람 모두 이동해야 함
    return (left_gap - 1) + (right_gap - 1)


# 함수 테스트
a, b, c = map(int, input().split())
print(continuous_nums(a, b, c))