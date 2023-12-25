def min_length_after_removing_one_segment(n, segments):
    """
    Calculate the minimum length of the shortest line segment that can contain
    all the remaining n - 1 line segments after removing one segment.

    :param n: Number of line segments
    :param segments: List of tuples representing the line segments (x1, x2)
    :return: Minimum length of the line segment to satisfy the condition
    """
    # Sort the segments based on the starting point
    segments.sort()

    # Initialize the minimum length required to encompass all segments except one
    min_length = float('inf')

    # Calculate the initial total length
    total_length = segments[-1][1] - segments[0][0]

    # Iterate over the segments and calculate the length if each segment is removed
    for i in range(n):
        if i == 0:
            # Length without the first segment
            current_length = segments[-1][1] - segments[1][0]
        elif i == n - 1:
            # Length without the last segment
            current_length = segments[-2][1] - segments[0][0]
        else:
            # Length without the i-th segment
            # Combine the segments before and after the i-th segment
            current_length = (segments[i - 1][1] - segments[0][0]) + (segments[-1][1] - segments[i + 1][0])
            current_length = min(current_length, total_length - (segments[i][1] - segments[i][0]))

        # Update the minimum length
        min_length = min(min_length, current_length)

    return min_length

n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

min_length = min_length_after_removing_one_segment(n, segments)

print(min_length)