from itertools import product

def evaluate_expression(expression, values):
    """
    주어진 값을 기반으로 식을 평가합니다.
    모든 연산의 우선순위가 동일하므로 왼쪽에서 오른쪽으로 계산합니다.
    """
    # 알파벳을 값으로 치환
    for var, val in values.items():
        expression = expression.replace(var, str(val))

    # 왼쪽에서 오른쪽으로 순차 계산
    tokens = list(expression)
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        i += 2

    return result

def maximize_expression(expression):
    """
    식의 결과를 최대로 만드는 값을 찾습니다.
    """
    # 식에서 등장하는 알파벳 추출
    variables = sorted(set(filter(str.isalpha, expression)))

    max_result = -2**31  # 초기 최대값 설정

    # 가능한 모든 조합 탐색 (1~4의 값을 각 변수에 배정)
    for values in product(range(1, 5), repeat=len(variables)):
        value_map = dict(zip(variables, values))
        result = evaluate_expression(expression, value_map)
        max_result = max(max_result, result)

    return max_result

# 입력 처리
expression = input().strip()
print(maximize_expression(expression))
