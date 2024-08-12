string = input()
n = len(string)

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if string[i - 1] == '(' and string[i] == '(' and string[j] == ')' and string[j + 1] == ')':
            cnt += 1

print(cnt)