def permute(n, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
    else:
        for i in range(1, n+1):
            if i not in seq:
                permute(n, seq + [i])

n = int(input())
permute(n, [])