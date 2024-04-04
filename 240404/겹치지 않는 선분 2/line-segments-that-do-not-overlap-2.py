def main():
    n = int(input())
    lines = []
    for _ in range(n):
        x1, x2 = map(int, input().split())
        lines.append((x1, x2))

    lines.sort(key=lambda x: x[1])

    count = 0
    end = lines[0][1]
    for i in range(1, n):
        if lines[i][0] >= end:
            count += 1
            end = lines[i][1]

    print(count)

if __name__ == '__main__':
    main()