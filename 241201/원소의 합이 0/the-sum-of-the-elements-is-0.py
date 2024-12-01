from collections import defaultdict

def count_zero_sums(n, A, B, C, D):
    # Step 1: 두 수열 A, B의 모든 가능한 합을 계산하여 그 빈도를 저장합니다.
    sum_ab = defaultdict(int)
    for a in A:
        for b in B:
            sum_ab[a + b] += 1

    # Step 2: 두 수열 C, D의 합이 -(A+B)의 형태가 되는 경우를 찾아 개수를 셉니다.
    count = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in sum_ab:
                count += sum_ab[target]

    return count

# 입력 처리
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = count_zero_sums(n, A, B, C, D)
print(result)