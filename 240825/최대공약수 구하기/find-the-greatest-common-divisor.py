def find_gcd(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    print(gcd)

n, m = map(int, input().split())
find_gcd(n, m)