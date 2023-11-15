n = int(input())
n_arr = list(map(int, input().split()))

sum_val = 0
sum_arr = []

for number in n_arr:
    sum_val += number
    if sum_val < 0:
        sum_val = 0
    sum_arr.append(sum_val)

print(max(sum_arr))