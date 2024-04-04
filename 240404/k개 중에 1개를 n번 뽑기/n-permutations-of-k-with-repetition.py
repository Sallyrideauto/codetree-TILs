def main():
    k, n = map(int, input().split())
    if k == 1 and n == 1:
        print('1')
    else:
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                print(i, j)

if __name__ == '__main__':
    main()