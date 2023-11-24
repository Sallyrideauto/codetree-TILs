n = int(input())

A_score = 0
B_score = 0
change = 0

current_leaders = {'A', 'B'}    # 처음에는 A와 B가 모두 리더

for _ in range(n):
    c, s = input().split()
    s = int(s)

    if c == 'A':
        A_score += s
    elif c == 'B':
        B_score += s

    new_leaders = set()
    if A_score > B_score:
        new_leaders.add('A')
    elif B_score > A_score:
        new_leaders.add('B')
    else:
        new_leaders = {'A', 'B'}

    if new_leaders != current_leaders:
        change += 1
        current_leaders = new_leaders


print(change)