n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

# 가능한 초기값 x를 1부터 10000까지 시도합니다.
for x in range(1, 10001):
    current_value = x
    valid = True
    
    for a, b in ranges:
        current_value *= 2
        if current_value < a or current_value > b:
            valid = False
            break
    
    if valid:
        print(x)
        break