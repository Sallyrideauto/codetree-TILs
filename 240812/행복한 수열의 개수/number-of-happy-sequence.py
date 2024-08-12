def is_happy_sequence(sequence, m):
    # If m is 1, every sequence with at least one element is happy.
    if m == 1:
        return True
    
    count = 1
    for i in range(1, len(sequence)):
        # Check if the current element is the same as the previous one.
        if sequence[i] == sequence[i-1]:
            count += 1
            # If we have found m consecutive elements, return True.
            if count >= m:
                return True
        else:
            # Reset count if the sequence is broken.
            count = 1
    return False

def happy_sequences(grid, n, m):
    happy_count = 0
    
    # Check for happy sequences in each row.
    for row in grid:
        if is_happy_sequence(row, m):
            happy_count += 1
    
    # Check for happy sequences in each column.
    for col in range(n):
        # Extract the column from the grid.
        column = [grid[row][col] for row in range(n)]
        if is_happy_sequence(column, m):
            happy_count += 1
            
    return happy_count

n, m = map(int, input().split())

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(happy_sequences(grid, n, m))