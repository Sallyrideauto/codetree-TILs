def find_abc(numbers):
    # Sort the input numbers
    sorted_numbers = sorted(numbers)

    # The largest number is A + B + C
    total_sum = sorted_numbers[-1]

    # The smallest number is A and the second smallest is B
    A = sorted_numbers[0]
    B = sorted_numbers[1]

    # C can be calculated as total_sum - A - B
    C = total_sum - A - B

    return A, B, C

# Reading input and converting it to a list
numbers = list(map(int, input().split()))

# Ensure there are exactly 7 numbers
if len(numbers) != 7:
    raise ValueError("Invalid input: exactly 7 numbers are required")

A, B, C = find_abc(numbers)
print(A, B, C)