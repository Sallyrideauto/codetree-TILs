def find_max_h(N, L, nums):
    for H in range(N, -1, -1):  # H 점수를 N부터 0까지 확인
        cnt_L = 0
        cnt_H = 0
        for num in nums:
            if num >= H:    # 현재 숫자가 H 이상이면
                cnt_H += 1
            elif num == H - 1:  # 현재 숫자가 H - 1이면
                cnt_H += 1
                cnt_L += 1

        if cnt_H >= H and (cnt_L - (cnt_H - H)) <= L:
            return H

    return 0    # H 점수가 0일 때

N, L = map(int, input().split())
nums = list(map(int, input().split()))

result = find_max_h(N, L, nums)
print(result)