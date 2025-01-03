from itertools import product

def evaluate_expression(expression, values):
    value_map = {chr(ord('a') + i): values[i] for i in range(len(values))}
    current_value = value_map.get(expression[0], 0)
    
    for i in range(1, len(expression), 2):
        op = expression[i]
        next_char = expression[i + 1]
        next_value = value_map.get(next_char, 0)
        if op == '+':
            current_value += next_value
        elif op == '-':
            current_value -= next_value
        elif op == '*':
            current_value *= next_value
    
    return current_value

def maximize_expression(expression):
    # Each letter can take a value from 1 to 4
    unique_variables = sorted(set([ch for ch in expression if ch.isalpha()]))
    max_result = -2**31
    
    # Generate all combinations of possible values for the variables
    for values in product(range(1, 5), repeat=len(unique_variables)):
        value_map = {var: val for var, val in zip(unique_variables, values)}
        result = evaluate_expression(expression, values)
        max_result = max(max_result, result)
    
    return max_result

# Example Usage
expression = input().strip()
print(maximize_expression(expression))
