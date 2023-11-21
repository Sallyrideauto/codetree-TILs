def max_distance(N, seats):
    # 좌석 간격과 최대 거리를 저장하는 변수
    max_gap = 0

    # 현재 간격을 측정하기 위한 변수
    current_gap = 0

    for seat in seats:
        # 현재 좌석이 비어 있으면 간격을 증가시킴
        if seat == '0':
            current_gap += 1
        else:
            # 좌석이 차 있으면 최대 간격 업데이트 후 간격 초기화
            max_gap = max(max_gap, current_gap)
            current_gap = 0

    # 마지막 구간의 간격도 확인
    max_gap = max(max_gap, current_gap)

    # 새로운 사람을 추가했을 때 최대 거리 계산
    return (max_gap + 1) // 2

N = int(input())
seats = input()

print(max_distance(N, seats))