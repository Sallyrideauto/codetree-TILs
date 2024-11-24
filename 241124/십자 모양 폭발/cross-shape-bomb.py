def explode_and_apply_gravity(n, grid, r, c):
    # Step 1: Explosion
    bomb_value = grid[r][c]
    directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    affected_positions = set()
    
    for i in range(bomb_value):
        for dr, dc in directions:
            new_r = r + dr * i
            new_c = c + dc * i
            if 0 <= new_r < n and 0 <= new_c < n:
                affected_positions.add((new_r, new_c))

    for ar, ac in affected_positions:
        grid[ar][ac] = 0
    
    # Step 2: Apply Gravity
    for col in range(n):
        stack = []
        for row in range(n - 1, -1, -1):
            if grid[row][col] != 0:
                stack.append(grid[row][col])
        for row in range(n - 1, -1, -1):
            if stack:
                grid[row][col] = stack.pop(0)
            else:
                grid[row][col] = 0

    return grid

# Read inputs
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Adjust indices to be zero-based
r -= 1
c -= 1

# Process the grid
grid = explode_and_apply_gravity(n, grid, r, c)

# Print the result
for row in grid:
    print(" ".join(map(str, row)))
