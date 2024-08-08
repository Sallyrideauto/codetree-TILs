def restore_sequence(N, sums):
    from itertools import permutations

    # 모든 가능한 수열을 생성
    possible_sequences = permutations(range(1, N + 1))

    # 사전순으로 가장 앞선 수열을 찾기
    for sequence in possible_sequences:
        valid = True
        for i in range(N - 1):
            if sequence[i] + sequence[i + 1] != sums[i]:
                valid = False
                break
        if valid:
            return sequence

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    sums = list(map(int, data[1:]))

    result = restore_sequence(N, sums)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()