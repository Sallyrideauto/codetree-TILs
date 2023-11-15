def min_time_to_reach_optimized(X):
    # dp[거리] = 최소 시간
    # 초기 속도는 1m/s, 최대 시간은 X를 넘지 않음
    dp = [float('inf')] * (X + 1)
    dp[1] = 1  # 거리 1m에 도달하는데 필요한 최소 시간은 1초

    # 가능한 모든 거리에 대해 최소 시간을 계산
    for distance in range(1, X):
        if dp[distance] == float('inf'):
            continue

        time = dp[distance]
        # 현재 거리에서 1m/s 증가, 유지, 감소하는 경우를 고려
        for speed_change in [-1, 0, 1]:
            new_speed = distance // time + speed_change
            if new_speed <= 0:
                continue
            new_distance = distance + new_speed
            if new_distance <= X:
                dp[new_distance] = min(dp[new_distance], time + 1)

    return dp[X] if dp[X] != float('inf') else -1  # 목적지에 도달하는 것이 불가능한 경우 -1 반환

# 예제 입력
X = int(input())

# 함수 실행 및 결과 출력
print(min_time_to_reach_optimized(X))