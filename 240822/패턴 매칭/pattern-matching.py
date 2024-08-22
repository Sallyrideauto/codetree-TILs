def is_match(s, p):
    # p가 빈 문자열인 경우, s도 빈 문자열이어야 매치됨
    if not p:
        return not s

    # 첫 번째 문자가 일치하는지 확인(p의 첫 문자가 '.'이거나 s와 p의 첫 문자가 같은 경우)
    first_match = bool(s) and p[0] in {s[0], '.'}

    # 만약 p의 길이가 2 이상이고, 두 번째 문자가 '*'인 경우
    if len(p) >= 2 and p[1] == '*':
        # '*' 전의 문자를 사용하지 않거나, 하나 사용하고 나머지 s와 p를 재귀적으로 확인
        return (is_match(s, p[2:]) or first_match and is_match(s[1:], p))
    else:
        # 다음 문자로 넘어가서 재귀적으로 매치 확인
        return first_match and is_match(s[1:], p[1:])

s = input()
p = input()

print("true" if is_match(s, p) else "false")