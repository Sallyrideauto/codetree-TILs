def process_commands():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    n = int(data[0])    # 첫 줄에서 명령의 수 n을 읽음
    commands = data[1:n + 1]    # 다음 n개의 줄에 대한 명령을 읽음

    hashmap = {}
    results = []

    for command in commands:
        parts = command.split()
        operation = parts[0]
        key = int(parts[1])

        if operation == "add":
            # 'add k v' 명령 처리: hashmap에 (k, v) 쌍을 추가하거나 업데이트
            value = int(parts[2])
            hashmap[key] = value
        elif operation == "remove":
            # 'remove k' 명령 처리: k 키를 가진 요소를 hashmap에서 제거
            if key in hashmap:
                del hashmap[key]
        elif operation == "find":
            # 'find k' 명령 처리: k 키를 가진 요소의 값을 찾아 결과 리스트에 추가
            value = hashmap.get(key, None)
            results.append(value)

    return results

# 결과 출력
if __name__ == "__main__":
    output = process_commands()
    for value in output:
        if value in output:
            if value is None:
                print("None")
            else:
                print(value)