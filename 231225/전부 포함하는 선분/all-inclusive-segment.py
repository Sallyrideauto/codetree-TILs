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

    # Initialize variables to store the start of the first segment and end of the last segment
    first_start = segments[0][0]
    last_end = segments[-1][1]

    # Initialize the minimum length after removal as a large number
    min_length = last_end - first_start

    # Calculate the minimum length for each segment when it is removed
    for i in range(n):
        if i == 0:
            # If the first segment is removed
            next_start = segments[1][0]
            length = last_end - next_start
        elif i == n - 1:
            # If the last segment is removed
            prev_end = segments[-2][1]
            length = prev_end - first_start
        else:
            # For middle segments, calculate the gap between the previous segment's end and the next segment's start
            prev_end = segments[i - 1][1]
            next_start = segments[i + 1][0]
            length = last_end - first_start - (next_start - prev_end)

        # Update the minimum length
        min_length = min(min_length, length)

    return min_length
    
n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

min_length = min_length_after_removal(n, segments)

print(min_length)