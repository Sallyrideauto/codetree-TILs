from itertools import combinations

def min_difference_partition():
    n = int(input())
    numbers = list(map(int, input().split()))

    # 전체 리스트의 합을 미리 계산
    total_sum = sum(numbers)
    # 최소 차이를 매우 큰 값으로 초기 설정
    min_difference = float('inf')

    # 2n개 중에서 n개를 선택하는 모든 조합 생성
    for comb in combinations(numbers, n):
        # 현재 조합의 합을 계산
        current_sum = sum(comb)
        # 나머지 원소들의 합은 전체 합에서 현재 조합의 합을 뺀 값
        remaining_sum = total_sum - current_sum
        # 두 합의 차의 절대값 계산
        difference = abs(current_sum - remaining_sum)
        # 차이의 최소값을 업데이트
        if difference < min_difference:
            min_difference = difference

    print(min_difference)

min_difference_partition()