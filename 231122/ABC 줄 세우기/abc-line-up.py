def minimum_swaps_to_sort(n, sequence):
    # 문자열을 리스트로 변환
    sequence = list(sequence.split())

    # 교환 횟수 계산
    swap_count = 0
    for i in range(n):
        for j in range(n - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                swap_count += 1

    return swap_count

n = int(input())
sequence = input()

print(minimum_swaps_to_sort(n, sequence))