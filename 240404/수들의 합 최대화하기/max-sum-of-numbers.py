from itertools import permutations

def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(max(sum(grid[i][j] for i, j in enumerate(perm)) for perm in permutations(list(range(n)))))

if __name__ == '__main__':
    main()