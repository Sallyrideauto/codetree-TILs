a, b = map(int, input().split())
c, d = map(int, input().split())

arr = [a, b, c, d]

min_arr = min(arr)
max_arr = max(arr)

cleaned = 0

for i in range(min_arr, max_arr):
    cleaned += 1
    
print(cleaned)