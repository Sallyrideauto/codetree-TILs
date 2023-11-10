n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(min_val):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem >= min_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > k:
            return False

    return True

maximin = 0
for i in range(1, min(arr[0], arr[-1]) + 1):
    if is_possible(i):
        maximin = max(maximin, i)

print(maximin)