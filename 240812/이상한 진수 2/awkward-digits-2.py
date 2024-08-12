import sys
INT_MIN = -sys.maxsize

binary = list(map(int, list(input())))
length = len(binary)

# 각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구하기
ans = INT_MIN
for i in range(length):
    # i번째 자릿수 변경
    binary[i] = 1 - binary[i]

    # 십진수로 변환
    num = 0
    for j in range(length):
        num = num * 2 + binary[j]

    ans = max(ans, num)

    # i번째 자릿수를 원래대로 반환
    binary[i] = 1 - binary[i]

print(ans)