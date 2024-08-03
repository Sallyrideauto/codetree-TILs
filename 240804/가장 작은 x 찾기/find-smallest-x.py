n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

# x의 초기 범위는 첫 번째 조건의 범위로 설정
min_x, max_x = ranges[0]

# 가능한 최소 x 탐색
result = None

for x in range(min_x, max_x + 1):
    valid = True
    current_value = x
    
    for a, b in ranges:
        current_value *= 2
        if current_value < a or current_value > b:
            valid = False
            break
        
    if valid:
        result = x
        break
    
print(result)