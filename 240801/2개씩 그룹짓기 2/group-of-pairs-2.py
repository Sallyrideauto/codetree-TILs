def max_min_pair_difference(n, nums):
    # 입력 리스트 정렬
    nums.sort()
    
    # 인접한 숫자끼리 그룹화하여 각 그룹의 차이 계산
    min_differences = []
    for i in range(len(nums)):
        min_differences.append(nums[i - 1] - nums[i])
        
    # 각 그룹의 차이 중 최소값 구하기
    return abs(min(min_differences))
    
n = int(input().strip())
nums = list(map(int, input().strip().split()))

print(max_min_pair_difference(n, nums))