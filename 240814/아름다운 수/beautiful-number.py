def is_beautiful_number(number):
    # 숫자를 문자열로 받아서 처리
    s = str(number)
    n = len(s)

    i = 0
    while i < n:
        count = 1

        # 현재 숫자와 다음 숫자가 같은지 검사
        while i + 1 < n and s[i] == s[i + 1]:
            count += 1
            i += 1

        # 숫자만큼의 연속성이 있는지 검사
        if count != int(s[i]):
            return False

        i += 1

    return True

def count_beautiful_numbers(n):
    beautiful_count = 0

    # 1부터 4까지의 숫자로 n자리 수 만들기(중복 조합)
    def generate_numbers(current_number):
        nonlocal beautiful_count

        if len(current_number) == n:
            if is_beautiful_number(current_number):
                beautiful_count += 1
            return

        for digit in range(1, 5):
            generate_numbers(current_number + str(digit))

    for digit in range(1, 5):
        generate_numbers(str(digit))

    return beautiful_count

n = int(input().strip())
print(count_beautiful_numbers(n))