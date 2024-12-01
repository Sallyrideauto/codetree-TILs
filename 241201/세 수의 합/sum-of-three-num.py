def count_combinations(nums, k):
    n = len(nums)
    count = 0

    # 세 개의 포인터를 사용하는 방식으로 문제를 해결합니다.
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for l in range(j + 1, n):
                if nums[i] + nums[j] + nums[l] == k:
                    count += 1

    return count

# 입력 처리
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 조합의 개수 출력
print(count_combinations(nums, k))
