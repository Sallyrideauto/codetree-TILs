'''
이 문제는 최소 힙(min heap) 자료구조를 사용하여 효율적으로 해결할 수 있는데, 
이는 매번 가장 짧은 두 막대를 찾아서 결합하는 과정을 용이하게 해줍니다. 
각 결합에 필요한 비용은 두 막대의 길이를 곱한 값이며, 모든 막대가 하나로 결합될 때까지 이 과정을 반복하게 됩니다.
'''

import heapq

def min_cost_to_combine_sticks(stick_lengths):
    # 최소 힙 생성
    heapq.heapify(stick_lengths)

    total_cost = 0

    # 막대가 하나면 남을 때까지 반복
    while len(stick_lengths) > 1:
        # 가장 짧은 두 막대를 꺼냄
        first = heapq.heappop(stick_lengths)
        second = heapq.heappop(stick_lengths)

        # 두 막대를 결합하는 비용을 계산
        cost = first * second
        total_cost += cost

        # 결합된 막대를 다시 힙에 추가
        heapq.heappush(stick_lengths, first + second)

    return total_cost

n = int(input())
sticks = list(map(int, input().split()))

print(min_cost_to_combine_sticks(sticks))