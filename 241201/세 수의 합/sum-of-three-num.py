from itertools import combinations

def count_combinations(nums, k):
    count = 0
    # itertools의 combinations를 사용해 nums 리스트에서 3개의 원소를 고르는 모든 조합을 구합니다.
    for comb in combinations(range(len(nums)), 3):
        # 각 조합의 세 원소의 합이 k와 같다면 카운트를 증가시킵니다.
        if nums[comb[0]] + nums[comb[1]] + nums[comb[2]] == k:
            count += 1
    return count

# 입력 처리
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 조합의 개수 출력
print(count_combinations(nums, k))