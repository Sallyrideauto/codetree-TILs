def max_distance_between_people(N, seating):
    # 빈 공간의 시작과 끝 인덱스를 찾는 함수
    def find_empty_spaces(seating):
        spaces = []
        start = None
        for i, seat in enumerate(seating):
            if seat == '0' and start is None:
                start = i
            elif seat == '1' and start is not None:
                spaces.append((start, i - 1))
                start = None
        if start is not None:
            spaces.append((start, N - 1))
        return spaces

    # 최대 거리 계산
    max_distance = 0
    for start, end in find_empty_spaces(seating):
        # 구간의 길이 계산
        length = end - start + 1

        # 양쪽 끝에 사람이 앉아 있는 경우
        if start > 0 and end < N - 1:
            distance = (length - 1) // 2
        # 한쪽 끝에만 사람이 앉아 있는 경우
        else:
            distance = length
        max_distance = max(max_distance, distance)

    return max_distance

N = int(input())
seating = input()

print(max_distance_between_people(N, seating))