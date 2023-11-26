import sys

def max_even_odd_groups(N, numbers):
    """
    Calculate the maximum number of groups that can be formed such that the sums alternate 
    between even and odd, starting with even.

    :param N: The number of numbers
    :param numbers: List of numbers
    :return: Maximum number of alternating sum groups
    """
    # Count the number of odd and even numbers
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    even_count = N - odd_count

    # If the counts of odd and even numbers are equal, the maximum number of groups
    # is equal to the count of either (since each group alternates between odd and even sums)
    if odd_count == even_count:
        return odd_count

    # If the counts are not equal, the maximum number of groups is the count of the smaller group plus one
    # This extra group is for the remaining numbers of the larger group
    return min(odd_count, even_count) + 1

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

print(max_even_odd_groups(N, numbers))