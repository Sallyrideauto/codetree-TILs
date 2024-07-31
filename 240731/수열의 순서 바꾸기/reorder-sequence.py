n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    flag = False
    for j in range(i, n - 1):
        if arr[j] > arr[j + 1]:
            flag = True
    if flag:
        cnt += 1

print(cnt)