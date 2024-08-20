def count_ways(n):
    MOD = 1000000007

    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 7
    elif n == 3:
        return 22

    # 이전 값들을 저장
    a, b, c, d = 1, 2, 7, 22

    for i in range(4, n + 1):
        # 새로운 값 계산
        next_val = (d * 2 + c * 3 + b) % MOD
        a, b, c, d = b, c, d, next_val

    return d

n = int(input())
print(count_ways(n))