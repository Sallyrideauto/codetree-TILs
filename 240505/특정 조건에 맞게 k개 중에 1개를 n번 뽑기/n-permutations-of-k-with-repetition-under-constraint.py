def generate_sequences(K, N, current_sequence = [], results = None):
    if results is None:
        results = []

    # 기본 조건: 길이 N에 도달했을 때 유효성 검사 후 결과에 추가
    if len(current_sequence) == N:
        results.append(current_sequence.copy())
        return

    # 재귀적 조건: 1부터 K까지 숫자를 시도
    for num in range(1, K + 1):
        if len(current_sequence) >= 2 and current_sequence[-1] == num and current_sequence[-2] == num:
            # 연속으로 같은 숫자가 이미 2개 있으므로 이번 숫자를 추가하면 3개가 됨
            continue
        current_sequence.append(num)
        generate_sequences(K, N, current_sequence, results)
        current_sequence.pop()
    
    return results

K, N = map(int, input().split())

# 모든 유효한 순서쌍 생성
sequences = generate_sequences(K, N)

for sequence in sequences:
    print(' '.join(map(str, sequence)))