n = int(input())

A_score, B_score, C_score = 0, 0, 0
change = 0

current_leaders = {'A', 'B', 'C'}    # 처음에는 A, B, C가 모두 리더

for _ in range(n):
    c, s = input().split()
    s = int(s)

    if c == 'A':
        A_score += s
    elif c == 'B':
        B_score += s
    elif c == 'C':
        C_score += s

    # 최고 점수 탐색
    max_score = max(A_score, B_score, C_score)

    # 리더 조합 결정
    new_leaders = set()
    if A_score == max_score:
        new_leaders.add('A')
    if B_score == max_score:
        new_leaders.add('B')
    if C_score == max_score:
        new_leaders.add('C')

    # 조합 변화 확인
    if new_leaders != current_leaders:
        change += 1
        current_leaders = new_leaders

print(change)