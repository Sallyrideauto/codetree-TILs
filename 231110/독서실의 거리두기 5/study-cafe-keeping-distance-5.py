N = int(input())
seats = input().strip()

# 최소 거리 계산
def calc_min_dist(distances):
    return max((d + 1) // 2 for d in distances)

# 1 사이의 거리 계산
def calc_distances(seats):
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
print(calc_min_dist(distances))