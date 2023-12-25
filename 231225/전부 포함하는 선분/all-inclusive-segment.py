def min_length_after_removal(n, segments):
    """
    Calculate the minimum length of the shortest line segment that can contain all 
    the remaining segments after removing one segment.

    :param n: Number of line segments
    :param segments: List of tuples representing the line segments (x1, x2)
    :return: Minimum length of the encompassing line segment after removal
    """
    # Sort the segments based on their starting and ending points
    segments.sort(key=lambda x: (x[0], x[1]))

    # Find the overall min start point and max end point
    min_start = segments[0][0]
    max_end = max(segments, key=lambda x: x[1])[1]

    # Initialize the minimum length after removal
    min_length = max_end - min_start

    # Calculate the length if each segment were removed
    for i in range(n):
        if i == 0:
            # If the first segment is removed
            new_min_start = segments[1][0]
        else:
            new_min_start = min_start

        if i == n - 1:
            # If the last segment is removed
            new_max_end = segments[-2][1]
        else:
            new_max_end = max(segments[i+1][1], max_end)

        # Update the minimum length after removal
        min_length = min(min_length, new_max_end - new_min_start)

    return min_length

n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

min_length = min_length_after_removal(n, segments)

print(min_length)