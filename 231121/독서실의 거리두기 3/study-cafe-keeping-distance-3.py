def max_distance(N, seats):
    # 빈 좌석 간격 리스트
    gaps = []
    current_gap = 0

    # 양쪽 끝 좌석이 비어있는지 확인
    left_end_empty = seats[0] == '0'
    right_end_empty = seats[-1] == '0'

    for seat in seats:
        if seat == '0':
            current_gap += 1
        else:
            if current_gap != 0:
                gaps.append(current_gap)
            current_gap = 0

    # 양 끝에 빈 좌석이 있으면 해당 간격을 추가
    if left_end_empty:
        gaps.append(gaps[0] if gaps else N)
    if right_end_empty:
        gaps.append(gaps[-1] if gaps else N)

    # 각 간격에서의 최대 거리 계산
    max_distance = 0
    for gap in gaps:
        if left_end_empty or right_end_empty:
            max_distance = max(max_distance, gap)
            left_end_empty = right_end_empty = False
        else:
            max_distance = max(max_distance, (gap + 1) // 2)

    return max_distance

# 예제 입력 테스트
N = int(input())
seats = input()

print(max_distance(N, seats))