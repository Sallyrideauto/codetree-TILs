x1, x2, y1, y2 = map(int, input().split())
a1, a2, b1, b2 = map(int, input().split())

a = []
b = []
c = []
d = []

for i in range(x1, y1 + 1):
    a.append(i)

for i in range(x2, y2 + 1):
    b. append(i)

for i in range(a1, b1 + 1):
    c.append(i)

for i in range(a2, b2 + 1):
    d.append(i)

arr_1 = list(set(a) & set(b))
arr_2 = list(set(c) & set(d))

if len(arr_1) == 0 and len(arr_2) == 0:
    print('nonoverlapping')
else:
    print('overlapping')