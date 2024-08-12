import sys

INT_MAX = sys.maxsize

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

min_dist = INT_MAX

# i번째 방에서 출발했을 경우의 결과를 구하기
for i in range(n):
    sum_dist = 0
    for j in range(n):
        dist = (j + n - i) % n
        sum_dist += dist * arr[j]

    # 가능한 거리의 합 중 최소값 구하기
    min_dist = min(min_dist, sum_dist)

print(min_dist)