def continuous_nums(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 왼쪽과 중간, 오른쪽과 중간 사이의 간격을 계산
    left_gap = positions[1] - positions[0]
    right_gap = positions[2] - positions[1]

    # 가장 작은 이동 횟수 계산
    # 두 사람이 이미 연속된 위치에 있는 경우는 한 명만 이동하면 됨
    return min(left_gap, right_gap) - 1

# 함수 테스트
a, b, c = map(int, input().split())
print(continuous_nums(a, b, c))