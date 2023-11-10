'''
문제의 요구사항을 다시 살펴보면, n개의 돌이 있고, 
각 돌에 적힌 숫자를 확인하면서 거리 k 이내로 점프하며 n번 돌에 도달하는 것이 목표입니다. 
여기서 중요한 점은 거쳐 간 돌들에 적힌 숫자들 중 최댓값이 최소가 되어야 한다는 것입니다.

이전 코드는 is_possible 함수에서 최솟값을 찾는 로직에 오류가 있습니다. 
is_possible 함수는 min_val보다 크거나 같은 숫자가 적힌 돌들만 고려하고 있으며, 
이렇게 될 경우 최댓값을 최소로 하는 조건을 충족하지 못할 수 있습니다.

문제를 해결하기 위해 다음과 같은 접근 방식을 사용할 수 있습니다:
1. 가능한 모든 숫자들의 최댓값에 대해 이진 탐색을 사용합니다. 이 때, 최솟값은 1이고 최댓값은 주어진 돌들 중 가장 큰 숫자입니다.
2. 중간값을 최대값으로 설정하고, 이 값을 만족하며 1번 돌에서 n번 돌로 이동할 수 있는지 확인합니다.
3. 만약 이동할 수 있다면, 가능한 최댓값을 줄여 더 작은 최댓값을 찾습니다. 그렇지 않다면, 최댓값을 늘려 이동 가능한지 다시 확인합니다.

이 코드는 이진 탐색을 사용하여 최대값을 최소화하는 문제를 해결합니다. 
can_reach 함수는 주어진 최대값으로 1번 돌에서 n번 돌까지 이동할 수 있는지 확인하며, 이진 탐색은 가능한 최대값을 찾습니다.
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 주어진 최대값으로 n번 돌까지 도달할 수 있는지 확인
def can_reach(max_val):
    current = 0
    while current < n - 1:
        next_jump = min(current + k, n - 1)
        while next_jump > current and arr[next_jump] > max_val:
            next_jump -= 1
        if next_jump == current:
            return False
        current = next_jump
    return True

# 이진 탐색을 사용하여 최소의 최대값 탐색
low, high = 1, max(arr)
min_max_val = high
while low <= high:
    mid = (low + high) // 2
    if can_reach(mid):
        min_max_val = mid
        high = mid - 1
    else:
        low = mid + 1

print(min_max_val)