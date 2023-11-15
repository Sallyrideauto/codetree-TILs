def min_time_to_reach_corrected(X):
    # dp[시간][거리] = 속도
    # 초기 속도는 1m/s, 최대 시간은 X를 넘지 않음
    dp = [[float('inf')] * (X + 1) for _ in range(X + 1)]
    dp[1][1] = 1    # 시작 시간 1초, 거리 1m, 속도 1m/s

    # 가능한 모든 시간과 거리에 대해 계산
    for time in range(1, X):
        for distance in range(1, X):
            speed = dp[time][distance]
            if speed == float('inf'):
                continue

            # 속도를 유지하는 경우
            if distance + speed <= X:
                dp[time + 1][distance + speed] = min(dp[time + 1][distance + speed], speed)
            
            # 속도를 증가시키는 경우
            if distance + speed + 1 <= X:
                dp[time + 1][distance + speed + 1] = min(dp[time + 1][distance + speed + 1], speed + 1)

            # 속도를 감소시키는 경우(0m/s는 불가)
            if speed > 1 and distance + speed - 1 <= X:
                dp[time + 1][distance + speed - 1] = min(dp[time + 1][distance + speed - 1], speed - 1)

    # 목적지에 도달하는 최고 시간을 찾음
    min_time = float('inf')
    for time in range(1, X + 1):
        if dp[time][X] == 1:    # 목적지에 도착했고, 속도가 1m/s인 경우
            min_time = min(min_time, time)

    return min_time if min_time != float('inf') else -1 # 목적지에 도달하는 것이 불가능할 경우 -1 반환

X = int(input())

print(min_time_to_reach_corrected(X))