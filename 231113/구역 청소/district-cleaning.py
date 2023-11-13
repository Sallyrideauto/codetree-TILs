a, b = map(int, input().split())
c, d = map(int, input().split())

arr_A = []
arr_B = []

for i in range(a, b + 1):
    arr_A.append(i)

for i in range(c, d + 1):
    arr_B.append(i)

arr_zone = arr_A + arr_B
arr_zone = list(set(arr_zone))

print(len(arr_zone) - 1)