n, k = map(int, input().split())
coins = []

count = 0

for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse = True)

for coin in coins:
    count += k // coin
    k %= coin

print(count)