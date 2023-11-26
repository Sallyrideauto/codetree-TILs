import sys

def min_blocks_to_move(n, block_counts):
    total_blocks = sum(block_counts)
    target = total_blocks // n
    moves = 0

    for count in block_counts:
        moves += abs(count - target)

    return moves // 2

n = int(input())
blocks = [int(input()) for i in range(n)]

print(min_blocks_to_move(n, blocks))