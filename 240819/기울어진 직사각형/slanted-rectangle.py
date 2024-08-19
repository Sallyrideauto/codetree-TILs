from copy import deepcopy

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def rect_sum_of_grid(rect):
    return sum(
        [
            grid[row][col]
            for col in range(n)
            for row in range(n)
            if rect[row][col]
        ]
    )

def generate_rect_list(l):
    rect_list = []
    d_list = [
        [-1, 1], [-1, -1], [1, -1], [1, 1]
    ]

    def in_range(row, col):
        if row < 0 or l <= row:
            return False
        if col < 0 or n <= col:
            return False
        return True

    def dfs(piv, end_point, cur_point, rect):
        row, col = cur_point
        rect[row][col] = 1

        if piv == len(d_list):
            rect[row][col] = 0
            return

        end_row, end_col = end_point
        a_row, a_col = d_list[piv]
        n_row = row + a_row
        n_col = col + a_col

        if end_row == n_row and end_col == n_col:
            rect_list.append(deepcopy(rect))
            rect[row][col] = 0
            return
        
        if not in_range(n_row, n_col):
            rect[row][col] = 0
            return

        if rect[n_row][n_col]:
            rect[row][col] = 0
            return

        dfs(piv + 1, end_point, [n_row, n_col], rect)
        dfs(piv, end_point, [n_row, n_col], rect)

        rect[row][col] = 0

    for row in range(l - 1, 0, -1):
        for col in range(1, l):
            rect = [[0] * l for _ in range(l)]
            dfs(0, [row, col], [row, col], rect)

    return rect_list

max_sum = 0

for rect in generate_rect_list(n):
    max_sum = max(max_sum, rect_sum_of_grid(rect))

print(max_sum)