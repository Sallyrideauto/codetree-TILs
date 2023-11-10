'''
문제를 다시 살펴보면, 새로운 사람을 앉힐 때 이미 앉아 있는 사람들 사이에 최대한 멀리 떨어져 앉히는 것이 목표입니다. 
이를 위해 좌석 배열에서 연속된 빈 좌석(‘0’)의 그룹을 찾고, 각 그룹 내에서 새로운 사람을 앉혔을 때 양쪽에 가장 가까운 사람과의 거리를 계산해야 합니다.

1. 연속된 빈 좌석 그룹을 찾습니다.
2. 각 그룹에서 새로운 사람을 앉혔을 때, 양쪽에 가장 가까운 사람과의 최소 거리를 계산합니다.
3. 이 거리들 중 최대값을 찾습니다.
'''

def max_distance_to_sit(seats):
    N = len(seats)
    max_dist = 0

    # 시작점과 끝점이 비어 있는 경우를 고려합니다.
    if seats[0] == '0':
        i = 0
        while i < N and seats[i] == '0':
            i += 1
        max_dist = max(max_dist, i)

    if seats[-1] == '0':
        i = N - 1
        while i >= 0 and seats[i] == '0':
            i -= 1
        max_dist = max(max_dist, N - 1 - i)

    # 중간의 빈 좌석 그룹을 찾아 최대 거리를 계산합니다.
    i = 0
    while i < N:
        if seats[i] == '1':
            j = i + 1
            while j < N and seats[j] == '0':
                j += 1
            if j < N:
                max_dist = max(max_dist, (j - i) // 2)
            i = j
        else:
            i += 1

    return max_dist

# 입력 받기
N = int(input())
seats = input().strip()

# 최대 거리 출력
print(max_distance_to_sit(seats))