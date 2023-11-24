n = int(input())
original_array = list(map(int, input().split()))

sorted_array = sorted(original_array)

# 첫 번째로 작은 숫자 탐색
first_min = sorted_array[0]

# 두 번째로 작은 숫자를 찾기 위해 배열을 순회
second_min = None
for num in sorted_array:
    if num != first_min:
        second_min = num
        break

# 두 번째로 작은 숫자의 위치 탐색
if second_min is not None:
    position = original_array.index(second_min) + 1
    print(position)
else:
    # 두 번째로 작은 숫자가 없는 경우 -1 출력
    print(-1)