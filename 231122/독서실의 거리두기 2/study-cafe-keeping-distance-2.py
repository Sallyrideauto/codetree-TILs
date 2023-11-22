def max_distance_between_people(N, seating):
    # 빈 공간 찾기
    empty_spaces = []
    start = -1
    for i, seat in enumerate(seating):
        if seat == '1' and start == -1:
            start = i
        elif seat == '0' and (i == N-1 or seating[i+1] == '1') and start != -1:
            end = i if i != N-1 else i+1
            empty_spaces.append((start, end))
            start = -1

    # 가능한 최대 거리 계산
    max_distance = 0
    for start, end in empty_spaces:
        # 구간의 길이 계산
        length = end - start

        # 새로운 사람을 추가했을 때 생기는 최소 거리
        min_distance = length // 2 if length % 2 == 0 else (length // 2) + 1

        # 최대 거리 업데이트
        max_distance = max(max_distance, min_distance)

    return max_distance

N = int(input())
seating = input()

print(max_distance_between_people(N, seating))