def min_cost_to_limit_diff(n, k, numbers):
    # 수들을 정렬
    numbers.sort()

    min_cost = float('inf')

    # 가능한 최소값과 최대값의 범위 설정
    min_val = numbers[0]
    max_val = numbers[-1]

    # 가능한 값의 범위에서 시작하여 모든 구간을 검사
    for lower_bound in range(min_val, max_val + 1):
        upper_bound = lower_bound + k

        # 현재 구간에 대해 비용을 계산
        cost = 0
        for num in numbers:
            if num < lower_bound:
                cost += lower_bound - num
            elif num > upper_bound:
                cost += num - upper_bound

        # 최소 비용 업데이트
        min_cost = min(min_cost, cost)

    return min_cost

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
numbers = list(map(int, data[2:]))

result = min_cost_to_limit_diff(n, k, numbers)
print(result)