n, m = map(int, input().split())
ans = []

def find_ans(depth, b):
    if depth == m:
        print(*ans)
        return
    for i in range(b, n + 1):
        if i not in ans:
            ans.append(i)
            find_ans(depth + 1, i)
            ans.pop()

find_ans(0, 1)