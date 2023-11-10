'''
제공된 입력 케이스에서 예상되는 출력이 올바르게 나오지 않는 것을 감안하여, 문제 해결 방식을 다시 살펴보겠습니다. 
목표는 각 돌을 건너뛰며 이동할 때, 거쳐간 돌들 중 최댓값이 최소가 되도록 하는 것입니다.

이를 위해서는 다음과 같은 방식으로 접근할 수 있습니다:
1. 가능한 모든 숫자들의 최댓값을 고려하여 이진 탐색을 사용합니다.
2. 각 이진 탐색 단계에서, 해당 최댓값을 초과하지 않는 한에서 최대한 멀리 떨어진 돌로 점프해야 합니다.
3. 만약 이러한 점프가 불가능하면 최댓값을 증가시켜야 하고, 가능하다면 최댓값을 감소시킬 수 있습니다.

이 코드는 각 이진 탐색 단계에서 최댓값을 기준으로 n번 돌까지 도달할 수 있는지 검사합니다. 
can_reach 함수는 주어진 최댓값을 초과하지 않는 한에서 최대한 멀리 떨어진 돌로 점프하는 것을 시도합니다. 
이진 탐색은 최적의 최댓값을 찾기 위해 사용됩니다.
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def can_reach(max_val):
    current_pos = 0
    for _ in range(n):  # 최대 n번 점프
        next_pos = current_pos
        for jump in range(1, k + 1):  # 최대 k 거리만큼 점프
            if current_pos + jump >= n or arr[current_pos + jump] > max_val:
                break
            next_pos = current_pos + jump
        if next_pos == current_pos:  # 더 이상 점프할 수 없는 경우
            return False
        current_pos = next_pos
        if current_pos == n - 1:  # 마지막 돌에 도달한 경우
            return True
    return False

# 이진 탐색으로 최적의 최대값 찾기
low, high = min(arr), max(arr)
result = high
while low <= high:
    mid = (low + high) // 2
    if can_reach(mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)