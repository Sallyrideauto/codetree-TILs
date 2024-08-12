import sys

INT_MAX = sys.maxsize

n = int(input())
n_arr = list(map(int, input().split()))

min_dist = INT_MAX

for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j - i) * n_arr[j]

    min_dist = min(min_dist, sum_dist)

print(min_dist)