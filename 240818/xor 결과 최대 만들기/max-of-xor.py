from itertools import combinations

def find_max_xor(n, m, arr):
    max_xor = 0

    # m개의 숫자를 뽑을 수 있는 모든 조합 생성
    for comb in combinations(arr, m):
        # 현재 조합의 XOR 값 계산
        current_xor = 0
        for num in comb:
            current_xor ^= num

        # 최대값 갱신
        if current_xor > max_xor:
            max_xor = current_xor

    return max_xor

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(find_max_xor(n, m, arr))