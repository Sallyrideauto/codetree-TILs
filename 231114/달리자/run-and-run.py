'''
이 문제를 해결하기 위해서는 '그리디 알고리즘'을 사용할 수 있습니다.
큰 그림으로 보면, 각 집에서 필요한 사람 수 만큼 이동시키면서, 최소한의 거리만 이동하도록 하는 것이 목표입니다.

이를 위해 다음과 같은 접근 방식을 사용할 수 있습니다:

1. 왼쪽에서 오른쪽으로 진행하면서 각 집을 살펴봅니다.
2. 현재 집에 더 많은 사람이 필요하면 이전 집에서 사람을 이동시킵니다.
3. 현재 집에 더 적은 사람이 필요하다면, 다음 집으로 사람을 이동시키려고 합니다.
'''

def min_total_distance(N, A_arr, B_arr):
    # 이동 거리를 저장할 변수 초기화
    total_distance = 0

    # 현재 집에 남아 있는 사람 수를 추적하기 위한 변수
    remaining = 0

    # 각 집을 순회하면서 이동 거리 계산
    for i in range(N):
        # 현재 집에 필요한 사람 수와 남아 있는 사람 수 비교
        # 남은 사람이 더 많다면 다음 집으로 이동
        # 남은 사람이 더 적다면 이전 집에서 사람을 끌어옴
        remaining += A_arr[i] - B_arr[i]

        # 이동 거리 갱신(항상 양수 값을 유지하기 위해 절대값 사용)
        total_distance += abs(remaining)

    return total_distance

N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

print(min_total_distance(N, A_arr, B_arr))