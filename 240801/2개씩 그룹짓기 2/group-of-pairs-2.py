import sys
si = sys.stdin.readline

def max_min_pair_difference(n, nums):
    # 입력 리스트 정렬
    nums.sort()
    
    # 인접한 숫자끼리 그룹화하여 각 그룹의 차이 계산
    min_differences = sys.maxsize
    for i in range(1, n + 1):
        min_differences = min(min_differences, nums[n + i] - nums[i])
        
    # 각 그룹의 차이 중 최소값 구하기
    return min_differences
    
n = int(si())
nums = [0] + list(map(int, si().split()))

print(max_min_pair_difference(n, nums))