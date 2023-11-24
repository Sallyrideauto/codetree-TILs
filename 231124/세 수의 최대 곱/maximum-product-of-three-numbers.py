n = int(input())
numbers = list(map(int, input().split()))

# 배열을 오름차순으로 정렬
numbers.sort()

# 가장 큰 세 양수의 곱
max1 = numbers[-1] * numbers[-2] * numbers[-3]

# 가장 큰 양수와 가장 큰 절대값을 가진 두 음수의 곱
max2 = numbers[0] * numbers[1] * numbers[-1]

# 두 경우 중 더 큰 값을 출력
print(max(max1, max2))