string = input()
n = len(string)

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if string[i] == '(' and string[j] == ')':
            cnt += 1

print(cnt)