N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    ans = 0
    for i in range(N):
        if arr[i] > arr[i + 1]:
            ans = i + 1
            break
    print(ans)