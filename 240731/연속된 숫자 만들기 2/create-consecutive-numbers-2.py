MAX_POS = 1000000
pos = list(map(int, input().split()))
swap_cnt = 0

while(True):
    a = abs(pos[0] - pos[1])
    b = abs(pos[1] - pos[2])
    
    # 각 둘씩 잡아서 거리가 전부 1이면 연속한 수
    if a == 1 and b == 1:
        break
    
    # 각 둘씩 잡았을 때 하나라도 거리가 2일 경우 한 번의 연산만 더 수행해주면 됨
    if a == 2 or b == 2:
        swap_cnt += 1
        break
    
    # 각 둘씩 잡았을 때 거리가 모두 2보다 클 경우 거리가 가까운 쪽 안에 반대편 수 삽입
    elif a > 2 and b > 2:
        if a < b:
            pos[1], pos[2] = pos[0] + 2, pos[1]
        else:
            pos[0], pos[1] = pos[1], pos[1] + 2
            
    elif abs(pos[1] - pos[2]) > 2:
        pos[0], pos[1] = pos[1], pos[1] + 2
        
    elif abs(pos[0] - pos[1]) > 2:
        pos[1], pos[2] = pos[0] + 2, pos[1]
        
    swap_cnt += 1
    
print(swap_cnt)