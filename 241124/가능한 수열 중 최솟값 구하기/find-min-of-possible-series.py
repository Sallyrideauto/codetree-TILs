def is_valid(sequence):
    length = len(sequence)
    for i in range(1, length // 2 + 1):
        if sequence[-i:] == sequence[-2 * i: -i]:
            return False
    return True

def find_sequence(n, sequence=""):
    if len(sequence) == n:
        return sequence

    for num in "456":
        new_sequence = sequence + num
        if is_valid(new_sequence):
            result = find_sequence(n, new_sequence)
            if result:
                return result

    return None

n = int(input())
result = find_sequence(n)
if result:
    print(result)
