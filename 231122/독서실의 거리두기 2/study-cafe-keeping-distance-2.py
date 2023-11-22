def max_distance_between_people(N, seating):
    # 빈 공간 찾기
    empty_spaces = []
    last_person = -1
    for i, seat in enumerate(seating):
        if seat == '1':
            if last_person != -1:
                empty_spaces.append((last_person, i))
            last_person = i
    
    # 각 구간에서의 최대 거리 계산
    max_distance = 0
    for start, end in empty_spaces:
        # 양쪽 끝에 사람이 앉아 있는 경우
        if start != 0 and end != N - 1:
            distance = (end - start) // 2
        # 한쪽 끝에만 사람이 앉아 있는 경우
        else:
            distance = end - start - 1
        max_distance = max(max_distance, distance)

    return max_distance


N = int(input())
seating = input()

print(max_distance_between_people(N, seating))