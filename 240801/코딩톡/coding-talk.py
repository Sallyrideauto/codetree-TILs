import sys

n, m, p = tuple(map(int, input().split()))
message = [
    list(input().split())
    for _ in range(m)
]

# 모두 읽은 채팅일 경우 읽지 않은 사람은 없음
if int(message[p - 1][1]) == 0:
    sys.exit()
    
# 각 사람에 대해 채팅을 읽었는지 여부 확인
for i in range(n):
    # read : 확실하게 채팅을 읽었을 경우 True
    person = chr(ord('A') + i)
    read = False
    
    # 만약 p번 메세지를 읽은 사람 수와 같은 채팅을 기준으로
    # 한 번이라도 채팅을 쳤다면 확실하게 채팅을 읽음
    for c, u in message:
        u = int(u)
        if u >= int(message[p - 1][1]) and c == person:
            read = True
            
    if read == False:
        print(person, end = " ")