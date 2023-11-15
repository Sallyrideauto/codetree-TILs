n = int(input())
n_arr = list(map(int, input().split()))

max_sum = n_arr[0]  # 첫 번째 원소로 초기화
current_sum = 0

for number in n_arr:
    current_sum += number
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0

print(max_sum)