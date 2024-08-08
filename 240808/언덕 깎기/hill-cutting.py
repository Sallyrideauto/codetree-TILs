def minimum_cost_to_adjust_heights(n, heights):
    heights.sort()  # 오름차순 정렬

    min_cost = float('inf') # 최소 비용 초기화

    # 가능한 최대 높이 차이는 17이므로, 시작 높이 h_min을 0에서 83까지 고려
    for h_min in range(0, 84):
        h_max = h_min + 17
        cost = 0

        for h in heights:
            if h < h_min:
                cost += (h_min - h) ** 2
            elif h > h_max:
                cost += (h - h_max) ** 2

        min_cost = min(min_cost, cost)

    return min_cost

import sys
input = sys.stdin.read

data = input().strip().split()
n = int(data[0])
heights = list(map(int, data[1:]))

print(minimum_cost_to_adjust_heights(n, heights))