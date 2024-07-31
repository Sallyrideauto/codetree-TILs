a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

area = [0] * 101

for i in range(a, b):
    area[i] = 1
    
for j in range(c, d):
    area[j] = 1
    
print(area.count(1))