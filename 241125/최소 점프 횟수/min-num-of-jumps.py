def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0
    if nums[0] == 0:
        return -1

    # 최대 도달 가능한 인덱스, 현재 점프에서 끝, 점프 횟수
    max_reach = nums[0]
    steps = nums[0]
    jumps = 1

    for i in range(1, n):
        # 마지막 위치에 도달한 경우
        if i == n - 1:
            return jumps
        
        # 최대 도달 가능한 위치 업데이트
        max_reach = max(max_reach, i + nums[i])

        # 현재 점프에서 사용할 수 있는 스텝 감소
        steps -= 1

        # 스텝이 0이 된 경우
        if steps == 0:
            # 점프를 해야 함
            jumps += 1

            # 현재 위치까지 도달 가능한지 확인
            if i >= max_reach:
                return -1
            
            # 새로운 스텝 카운트 설정
            steps = max_reach - i

    return -1

n = int(input())
nums = list(map(int, input().split()))

print(min_jumps(nums))