'''
이 문제를 해결하기 위해 다른 접근 방식이 필요합니다. 
문제의 목표는 거리 k 이내로 점프하며 n번 돌에 도달할 때, 거쳐간 지점에 적힌 숫자들 중 최댓값을 최소화하는 것입니다.

이 문제를 해결하기 위한 접근 방법은 다음과 같습니다:

1. 가능한 모든 점프 경로를 고려하여, 각 경로에서 거쳐가는 숫자들 중 최댓값을 찾습니다.
2. 이 최댓값들 중 최솟값을 찾습니다.

이 코드는 각 시작점에서 최대 k 만큼 점프할 수 있는 모든 경로를 고려하여, 그 경로에서의 최댓값을 찾은 다음 그 중 최솟값을 반환합니다.
이는 주어진 조건 하에서 최대한 거리를 두며 이동할 때, 거쳐가는 숫자들 중 최댓값을 최소화하는 경로를 찾는 것입니다.
'''

n, k = map(int, input().split())
stones = list(map(int, input().split()))

# 모든 경로를 탐색하여 각 경로의 최댓값 중 최솟값을 찾는 함수
def find_min_max(stones, k, n):
    min_max = float('inf')

    # 모든 가능한 시작 위치에서 탐색
    for start in range(n - 1):
        max_in_path = stones[start]

        # 최대 k만큼 점프
        for end in range(start + 1, min(start + k + 1, n)):
            max_in_path = max(max_in_path, stones[end])
            # 마지막 돌에 도달하면 최대값을 갱신
            if end == n - 1:
                min_max = min(min_max, max_in_path)

    return min_max

print(find_min_max(stones, k, n))