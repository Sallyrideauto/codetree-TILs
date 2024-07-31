import sys

N = int(input())
seated = list(map(int, input()))

def get_min_and_max_dist():
    min_dist = sys.maxsize
    max_dist = -sys.maxsize
    
    for i in range(N - 1):
        if seated[i] == 1:
            for j in range(i + 1, N):
                if seated[j] == 1:
                    dist = j - i
                    break
            min_dist = min(min_dist, dist)
            max_dist = max(max_dist, dist)
            
    return min_dist, max_dist
    
# 기존에 앉은 사람이 1일 경우 양 끝에 앉혔을 때 거리두기의 값이 큰 경우가 답
seat_count = seated.count(1)
if seat_count == 1:
    index = seated.index(1)
    print(max(index, N - 1 - index))
    sys.exit()
    
# 기존에 앉은 사람이 둘 이상인 경우
min_dist, max_dist = get_min_and_max_dist()
ans = 0

if min_dist <= max_dist // 2:
    ans = min_dist
else:
    ans = max_dist // 2
    
if seated[0] != 1:
    seated[0] = 1
    new_min_dist, new_max_dist = get_min_and_max_dist()
    ans = max(ans, new_min_dist)
    seated[0] = 0
    
if seated[N - 1] != 1:
    seated[N - 1] = 1
    new_min_dist, new_max_dist = get_min_and_max_dist()
    ans = max(ans, new_min_dist)
    seated[1] = 0
    
print(ans)