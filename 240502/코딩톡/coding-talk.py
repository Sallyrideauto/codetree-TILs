def find_unread_users(n, m, p, messages):
    users = [chr(ord('A') + i) for i in range(n)]
    # 각 사용자가 읽은 마지막 메시지 인덱스를 추적
    last_read = {user: -1 for user in users}
    
    # 메시지를 보낸 사람은 해당 메시지를 읽은 것으로 처리
    for i in range(m):
        sender, unread_count = messages[i]
        last_read[sender] = max(last_read[sender], i)
    
    # 각 메시지에 대해 읽지 않은 사람들을 업데이트
    for i in range(m):
        sender, unread_count = messages[i]
        if unread_count > 0:
            # 이 메시지를 읽지 않았을 사람들을 업데이트
            # 현재 메시지까지 읽은 사용자들을 제외한 나머지 사용자들은 이 메시지를 읽지 않았을 수 있음
            read_users = {user for user, idx in last_read.items() if idx >= i}
            unread_users = set(users) - read_users
            if len(unread_users) > unread_count:
                continue  # 읽지 않은 사람 수보다 많은 경우, 정확한 업데이트가 어려움
            for user in unread_users:
                last_read[user] = max(last_read[user], i - 1)

    # p번째 메시지를 읽지 않았을 가능성이 있는 사람을 찾기
    potential_unread = [user for user, last_msg_index in last_read.items() if last_msg_index < p - 1]
    return ' '.join(sorted(potential_unread))

def main():
    n, m, p = map(int, input().split())
    messages = []
    for _ in range(m):
        sender, unread_count = input().split()
        unread_count = int(unread_count)
        messages.append((sender, unread_count))
    
    result = find_unread_users(n, m, p, messages)
    print(result)

if __name__ == "__main__":
    main()