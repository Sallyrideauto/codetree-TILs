N = int(input())
seats = list(map(int, input()))

def get_minDist(arr):
    cnt = 0
    r = []
    
    for j in range(len(arr)):
        if arr[j] == 1:
            r.append(cnt)
            cnt = 0
        cnt += 1
    
    return min(r[1::])
    
ans = -1

for i in range(len(seats)):
    if seats[i] == 0:
        seats[i] = 1
        ans = max(get_minDist(seats), ans)
        seats[i] = 0
        
print(ans)