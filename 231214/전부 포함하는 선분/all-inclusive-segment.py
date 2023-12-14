def min_line_segments_coverage(n, segments):
    # Sort the line segments based on their starting point(x1)
    segments.sort(key = lambda x: x[0])

    # Find the maximum gap between consecutive segments
    max_gap = 0
    max_gap_index = 0
    for i in range(n - 1):
        gap = segments[i + 1][0] - segments[i][1]
        if gap > max_gap:
            max_gap = gap
            max_gap_index = i

    # Handle corner case when the maximum gap is at the beginning or the end
    if max_gap_index == 0 or max_gap_index == n - 2:
        if max_gap_index == 0:
            return segments[-1][1] - segments[1][0]
        else:
            return segments[-2][1] - segments[0][0]

    # Calculate the minimum coverage without the segment contributing to the maximum gap
    return segments[-1][1] - segments[0][0] - max_gap

n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

print(min_line_segments_coverage(n, segments))