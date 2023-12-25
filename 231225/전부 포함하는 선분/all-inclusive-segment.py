def min_length_after_removal(n, segments):
    """
    Calculate the minimum length of the shortest line segment that can contain all 
    the remaining segments after removing one segment.

    :param n: Number of line segments
    :param segments: List of tuples representing the line segments (x1, x2)
    :return: Minimum length of the encompassing line segment after removal
    """
    # Sort the segments based on their starting points
    segments.sort()

    # Initialize the minimum length after removal as a large number
    min_length = float('inf')

    # Calculate the minimum length for each segment when it is removed
    for i in range(n):
        if i == 0:
            # If the first segment is removed, consider the second segment's start to the last segment's end
            start = segments[1][0]
        else:
            start = segments[0][0]

        if i == n - 1:
            # If the last segment is removed, consider the first segment's start to the second last segment's end
            end = segments[-2][1]
        else:
            end = segments[-1][1]

        # Update the minimum length
        min_length = min(min_length, end - start)

    return min_length

n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

min_length = min_length_after_removal(n, segments)

print(min_length)