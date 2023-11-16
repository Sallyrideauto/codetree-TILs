def continuous_nums(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 가장 왼쪽 끝과 중간 사이, 그리고 중간과 가장 오른쪽 끝 사이 거리 계산
    left_gap = positions[1] - positions[0]
    right_gap = positions[2] = positions[1]

    # 만약 이미 연속된 숫자 위치라면 이동할 필요가 없음
    if left_gap == 1 and right_gap == 1:
        return 0

    # 더 큰 간격에서 한 칸을 더 이동해야 함
    # 하지만 이미 연속된 경우는 0 이동으로 처리
    return max(left_gap, right_gap) - 1
    

a, b, c = map(int, input().split())
print(continuous_nums(a, b, c))