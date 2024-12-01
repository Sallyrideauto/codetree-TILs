def count_pairs_with_sum(arr, k):
    seen = {}
    count = 0

    # Iterate over the array
    for num in arr:
        complement = k - num

        # Check if the complement is already in the dictionary
        if complement in seen:
            count += seen[complement]

        # Update the dictionary with the current number
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
print(count_pairs_with_sum(arr, k))
