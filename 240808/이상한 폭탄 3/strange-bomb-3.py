def find_most_exploded_bomb(N, K, bomb_numbers):
    from collections import defaultdict

    # Dictionary to kepp track of bomb explosions
    bomb_explosion_count = defaultdict(int)

    # Iterate through each bomb and check its distance with others
    for i in range(N):
        for j in range(i + 1, min(i + K + 1, N)):
            if bomb_numbers[i] == bomb_numbers[j]:
                bomb_explosion_count[bomb_numbers[i]] += 1
                bomb_explosion_count[bomb_numbers[j]] += 1

    # Find the bomb with the maximum explosion count
    max_explosions = 0
    max_exploede_bomb = 0

    for bomb, count in bomb_explosion_count.items():
        if count > max_explosions or (count == max_explosions and bomb > max_exploede_bomb):
            max_explosions = count
            max_exploede_bomb = bomb

    return max_exploede_bomb

# Reading input
N, K = map(int, input().split())
bomb_numbers = [int(input()) for _ in range(N)]

# Find and print the most exploded bomb number
result = find_most_exploded_bomb(N, K, bomb_numbers)
print(result)