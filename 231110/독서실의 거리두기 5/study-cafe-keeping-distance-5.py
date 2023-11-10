N = int(input())
seats = input().strip()

def calc_distances(seats):
    # '1' 사이의 거리와 시작점, 끝점으로부터의 거리 계산
    distances = []
    last_seat = -1
    for i, seat in enumerate(seats):
        if seat == '1':
            if last_seat != -1:
                distances.append(i - last_seat - 1)
            last_seat = i
    # 시작점과 첫 번째 '1' 사이, 마지막 '1'과 끝점 사이의 거리 추가
    if seats[0] == '0':
        distances.append(last_seat)
    if seats[-1] == '0':
        distances.append(len(seats) - last_seat - 1)
    return distances

distances = calc_distances(seats)

# 각 거리의 절반을 취하고, 그 중 최댓값을 찾습니다.
min_max_distance = max((d + 1) // 2 for d in distances)
print(min_max_distance)