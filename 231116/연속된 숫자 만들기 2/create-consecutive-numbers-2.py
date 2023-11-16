def continuous_nums(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 왼쪽과 중간, 오른쪽과 중간 사이의 간격을 계산
    left_gap = positions[1] - positions[0]
    right_gap = positions[2] - positions[1]

    # 이미 연속된 숫자 위치에 있는 경우
    if left_gap == 1 or right_gap == 1:
        return 0

    # 한 명만 이동하는 경우(한쪽 간격이 2)
    if left_gap == 2 or right_gap == 2:
        return 1

    # 두 명이 이동해야 하는 경우
    return 2


# 함수 테스트
a, b, c = map(int, input().split())
print(continuous_nums(a, b, c))