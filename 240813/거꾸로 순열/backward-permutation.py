def permute(n, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
    else:
        for i in range(n, 0, -1):
            # i를 n부터 1까지 감소하는 순서로 순회
            if i not in seq:
                permute(n, seq + [i])

n = int(input())
permute(n, [])