def find_abcd(numbers):
    sorted_numbers = sorted(numbers)

    # The largest number is A + B + C + D
    total_sum = sorted_numbers[-1]

    # The smallest number is A and the second smallest is B and the third smallest is C
    A = sorted_numbers[0]
    B = sorted_numbers[1]
    C = sorted_numbers[2]

    # D can be calculated as total_sum - A - B - C
    D = total_sum - A - B - C

    return A, B, C, D

numbers = list(map(int, input().split()))

if len(numbers) != 15:
    raise ValueError("Invalid Input")

A, B, C, D = find_abcd(numbers)
print(A, B, C, D)