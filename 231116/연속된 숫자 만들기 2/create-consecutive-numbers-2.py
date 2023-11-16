def continuous_nums(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 각 사이의 간격 계산
    left_gap = positions[1] - positions[0]
    right_gap = positions[2] - positions[1]

    # 이미 연속된 숫자 위치에 있는 경우
    if left_gap == 1 and right_gap == 1:
        return 0
    
    # 두 간격 중 큰 간격을 1 줄여서 연속된 숫자 위치로 만듦
    return max(left_gap, right_gap) - 1

# 함수 테스트
a, b, c = map(int, input().split())
print(continuous_nums(a, b, c))