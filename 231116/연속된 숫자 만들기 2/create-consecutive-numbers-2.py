def continuous_nums(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 각 사이의 간격 계산
    gap1 = positions[1] - positions[0]
    gap2 = positions[2] - positions[1]

    # 이미 연속된 숫자 위치에 있는 경우
    if gap1 == 1 and gap2 == 1:
        return 0
    
    # 한 쪽 간격이 1이고 다른 쪽 간격이 2 이상인 경우
    if gap1 == 1 or gap2 == 1:
        return 1

    # 두 간격 모두 2 이상인 경우
    return 2

# 함수 테스트
a, b, c = map(int, input().split())
print(continuous_nums(a, b, c))