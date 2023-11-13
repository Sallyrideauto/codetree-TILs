x1, x2, x3, x4 = map(int, input().split())
a = []
b = []

for i in range(x1, x2 + 1):
    a.append(i)

for i in range(x3, x4 + 1):
    b.append(i)

arr = list(set(a) & set(b))

if len(arr) == 0:
    print('nonintersecting')
else:
    print('intersecting')