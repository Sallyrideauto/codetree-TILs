def find_overlap(segments):
    # Initialize the overlap range with the first segment's start and end points.
    overlap_start, overlap_end = segments[0]

    # Iterate over all segments to find the common overlap range.
    for start, end in segments[1:]:
        # Update the start of the overlap to the maximum of the current start and the overlap_start.
        overlap_start = max(overlap_start, start)
        # Update the end of the overlap to the minimum of the current end and the overlap_end.
        overlap_end = min(overlap_end, end)

        # If the current overlap range is invalid(start > end), no common overlap exists.
        if overlap_start > overlap_end:
            return "No"
    
    # If the loop completes without returning "No", a common overlap exists.
    return "Yes"

n = int(input())

segments_info = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments_info.append((x1, x2))

print(find_overlap(segments_info))