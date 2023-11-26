import sys

def max_min_difference_in_groups(numbers):
    # Sort the numbers
    numbers.sort()

    # Initialize the maximum minimum difference
    max_min_diff = 0

    # Iterate over the sorted numbers and calculate the minimum difference in each group
    for i in range(0, len(numbers) - 1, 2):
        # Calculate the difference in the current group
        diff = numbers[i + 1] - numbers[i]

        # Update the maximum minimum difference
        max_min_diff = max(max_min_diff, diff)

    return max_min_diff

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

print(max_min_difference_in_groups(numbers))