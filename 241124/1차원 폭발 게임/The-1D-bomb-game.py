def collapse_bombs(n, m, bombs):
    # To simulate gravity, we use a list to represent the stack of bombs.
    stack = []

    for bomb in bombs:
        stack.append(bomb)

        # Check if the latest added bomb causes any explosion.
        while True:
            # Traverse the stack to identify consecutive segments of the same bomb value
            temp_stack = []
            i = 0
            while i < len(stack):
                j = i
                while j < len(stack) and stack[j] == stack[i]:
                    j += 1
                # If the length of the segment is greater than or equal to m, skip adding to temp_stack (simulate explosion)
                if j - i >= m:
                    i = j
                else:
                    temp_stack.extend(stack[i:j])
                    i = j
            
            # If no change, break the loop
            if len(temp_stack) == len(stack):
                break
            else:
                stack = temp_stack

    return stack


# Read inputs
n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

# Calculate final state of the bombs after all explosions
result = collapse_bombs(n, m, bombs)

# Output the result
print(len(result))
for bomb in result:
    print(bomb)