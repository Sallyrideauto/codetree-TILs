n, k = map(int, input().split())
n_arr = list(map(int, input().split()))

# 초기 슬라이딩 윈도우 합 계산
current_sum = sum(n_arr[:k])
max_sum = current_sum

# 슬라이딩 윈도우 이동
for i in range(k, n):
    # 새로운 윈도우 합 계산
    current_sum += n_arr[i] - n_arr[i - k]
    # 최대 합 업데이트
    if current_sum > max_sum:
        max_sum = current_sum
        
print(max_sum)