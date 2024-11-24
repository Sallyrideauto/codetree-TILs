def collapse_bombs(n, m, bombs):
    # To simulate gravity, we use a list to represent the stack of bombs.
    stack = []

    for bomb in bombs:
        stack.append(bomb)

        # Check if the latest added bomb causes any explosion.
        while len(stack) >= m:
            top_bombs = stack[-m:]
            if all(b == top_bombs[0] for b in top_bombs):
                # Remove the bombs from stack
                del stack[-m:]
                # Check if there are more consecutive numbers to remove.
                continue
            else:
                break

    return stack

n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

# Calculate final state of the bombs after all explosions
result = collapse_bombs(n, m, bombs)

print(len(result))
for bomb in result:
    print(bomb)