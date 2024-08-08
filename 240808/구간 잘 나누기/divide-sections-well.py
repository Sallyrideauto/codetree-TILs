def can_divide(nums, m, max_sum):
    current_sum = 0
    required_segments = 1
    for num in nums:
        if current_sum + num > max_sum:
            required_segments += 1
            current_sum = num
            if required_segments > m:
                return False
        else:
            current_sum += num
    return True

def find_minimum_max_sum(nums, m):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        if can_divide(nums, m, mid):
            right = mid
        else:
            left = mid + 1

    return left

n, m = map(int, input().split())
nums = list(map(int, input().split()))

print(find_minimum_max_sum(nums, m))