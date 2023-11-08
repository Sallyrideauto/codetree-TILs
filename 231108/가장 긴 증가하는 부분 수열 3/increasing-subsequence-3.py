'''
이 문제는 동적 프로그래밍(Dynamic Programming, DP)을 사용하여 해결할 수 있습니다. 
주어진 수열의 각 원소에 대해, 그 원소를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이를 계산합니다. 
각 원소에 대해, 그보다 앞에 위치하고 더 작은 원소들의 가장 긴 증가하는 부분 수열의 길이에 1을 더한 값 중 최대값을 선택하여 DP 테이블을 갱신합니다.
'''

def length_of_lis(nums):
    # DP 테이블 초기화 : 모든 위치에서의 최대 증가 부분 수열의 길이는 최소 1
    dp = [1] * len(nums)

    # 모든 원소에 대해 순회하며 DP 테이블을 갱신
    for i in range(1, len(nums)):
        for j in range(i):
            # nums[i]가 nums[j]보다 크다면, 증가 부분 수열을 만들 수 있음
            if nums[i] > nums[j]:
                # DP 테이블 갱신
                dp[i] = max(dp[i], dp[j] + 1)

    # 가장 긴 증가하는 부분수열의 길이를 반환
    return max(dp)

n = int(input())
nums = list(map(int, input().split()))

print(length_of_lis(nums))