from collections import deque

def min_time_to_reach_X(X):
    # 현재 상태를 나타내는 집합 (현재 거리, 현재 속도, 경과 시간)
    queue = deque([(0, 1, 1)])  # (distance, speed, time)
    visited = set((0, 1))  # (distance, speed)

    while queue:
        dist, speed, time = queue.popleft()
        
        # 목표 거리에 도달하고 속도가 1m/s 인 경우
        if dist == X and speed == 1:
            return time
        
        # 가능한 속도 변화는 -1, 0, +1
        for change in (-1, 0, 1):
            new_speed = speed + change
            new_dist = dist + new_speed
            
            # 유효한 속도 및 거리 확인 (0m/s가 되어서는 안됨)
            if new_speed > 0 and (new_dist, new_speed) not in visited:
                if new_dist <= X:
                    queue.append((new_dist, new_speed, time + 1))
                    visited.add((new_dist, new_speed))

# 입력 받기
X = int(input().strip())

# 최단 시간 계산
result = min_time_to_reach_X(X)

# 결과 출력
print(result)