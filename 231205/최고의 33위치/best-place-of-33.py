n = int(input())

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def get_num_of_coin(row, col):
    num_of_coin = 0

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            num_of_coin += grid[i][j]

    return num_of_coin

max_coin = 0

for row in range(n - 2):
    for col in range(n - 2):
        num_of_coin = get_num_of_coin(row, col)
        max_coin = max(max_coin, num_of_coin)

print(max_coin)