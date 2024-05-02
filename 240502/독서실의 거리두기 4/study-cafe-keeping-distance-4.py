from itertools import combinations

def calculate_min_distance(seats, idx1, idx2):
    # 두 개의 새 좌석에 사람을 배치
    n = len(seats)
    occupied = [i for i, seat in enumerate(seats) if seat == '1'] + [idx1, idx2]
    occupied.sort()

    # 배치 후 모든 인접한 좌석 사이의 최소 거리 계산
    min_distance = float('inf')
    for i in range(1, len(occupied)):
        min_distance = min(min_distance, occupied[i] - occupied[i - 1])

    return min_distance

def max_min_distance(n, seat_string):
    empty_indices = [i for i in range(n) if seat_string[i] == '0']
    max_distance = 0

    # 가능한 모든 두 빈 좌석의 조합 구하기
    for idx1, idx2 in combinations(empty_indices, 2):
        min_distance = calculate_min_distance(seat_string, idx1, idx2)
        max_distance = max(max_distance, min_distance)

    return max_distance

n = int(input())
seat_string = input()

print(max_min_distance(n, seat_string))