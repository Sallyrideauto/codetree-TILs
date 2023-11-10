'''
문제에 대한 이해를 바탕으로, 코드의 접근 방식을 다시 검토해보겠습니다. 
목표는 거리 k 이내로 점프하면서, 거쳐간 지점에 적혀있는 숫자들 중 최댓값을 최소로 하는 것입니다.

이를 위해선 두 가지 중요한 점을 고려해야 합니다:
1. 거리 k 이내에 점프할 수 있는지 확인.
2. 가능한 최대값을 최소로 만들 수 있는 경로 찾기.

이진 탐색을 사용하는 현재의 접근 방식은 올바른 방향이지만, 구현에서 문제가 있습니다. 
can_reach 함수가 주어진 최댓값으로 n번 돌까지 이동할 수 있는지를 확인하는 로직을 개선할 필요가 있습니다.

각 돌의 값이 최댓값보다 작거나 같을 때만 해당 돌로 이동할 수 있어야 합니다. 
이동할 수 있는 돌이 없을 경우는 최댓값을 늘려야 하며, n번 돌까지 도달할 수 있을 경우는 최댓값을 줄일 수 있습니다.
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

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