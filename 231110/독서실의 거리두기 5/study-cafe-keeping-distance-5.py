N = int(input())
seats = input().strip()

def find_max_distance(seats):
    last_occupied = -1
    max_distance = 0

    for i in range(N):
        if seats[i] == '1':
            if last_occupied == -1:
                # 시작점부터 첫 번째 '1'까지의 거리
                max_distance = max(max_distance, i)
            else:
                # '1'과 '1' 사이의 거리의 절반
                max_distance = max(max_distance, (i - last_occupied) // 2)
            last_occupied = i

    # 마지막 '1'부터 끝점까지의 거리
    if last_occupied != N - 1:
        max_distance = max(max_distance, N - 1 - last_occupied)

    return max_distance

print(find_max_distance(seats))