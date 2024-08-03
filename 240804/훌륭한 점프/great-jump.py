n, k = map(int, input().split())
n_arr = list(map(int, input().split()))

def can_reach_with_max_value(max_val):
    current_position = 0
    while current_position < n - 1:
        next_position = -1
        for i in range(1, k + 1):
            if current_position + i < n and n_arr[current_position + i] <= max_val:
                next_position = current_position + i
        if next_position == -1:
            return False
        current_position = next_position
    return True

left = max(n_arr[0], n_arr[-1])
right = max(n_arr)
result = right

while left <= right:
    mid = (left + right) // 2
    if can_reach_with_max_value(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)