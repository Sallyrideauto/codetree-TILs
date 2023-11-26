import sys

def longest_increasing_subsequence(sequence):
    """
    Calculate the length of the longest increasing subsequence in the sequence.

    :param sequence: List of integers representing the sequence
    :return: Length of the longest increasing subsequence
    """
    if not sequence:
        return 0

    # Initialize LIS length array
    lis = [1] * len(sequence)

    # Compute optimized LIS values in a bottom-up manner
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # The maximum value in lis[] is the length of the LIS
    return max(lis)

def min_moves_to_sort(N, sequence):
    # Find the length of the longest increasing subsequence
    lis_length = longest_increasing_subsequence(sequence)

    # The minimum number of moves is the total length minus the length of the LIS
    return N - lis_length

N = int(input())
sequence = list(map(int, sys.stdin.readline().split()))

print(min_moves_to_sort(N, sequence))