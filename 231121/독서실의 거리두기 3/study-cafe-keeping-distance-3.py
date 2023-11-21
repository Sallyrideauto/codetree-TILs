def max_distance(N, seats):
    # 좌석 간격과 최대 거리를 저장하는 변수
    max_gap = 0

    # 현재 간격을 측정하기 위한 변수
    current_gap = 0
    
    # 첫 번째 사람을 만날 때까지의 간격
    first_person = seats.find('1')
    last_person = seats.rfind('1')

    # 첫 번째와 마지막 사람 사이의 간격만 고려
    for i in range(first_person, last_person + 1):
        # 현재 좌석이 비어 있으면 간격을 증가시킴
        if seats[i] == '0':
            current_gap += 1
        else:
            # 좌석이 차 있으면 최대 간격 업데이트 후 간격 초기화
            max_gap = max(max_gap, current_gap)
            current_gap = 0

    # 새로운 사람을 추가했을 때의 최대 거리 계산
    return max(first_person, (max_gap + 1) // 2, N - last_person - 1)

N = int(input())
seats = input()

print(max_distance(N, seats))