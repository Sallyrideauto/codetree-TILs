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

# 두 번째로 작은 숫자의 위치와 유일성을 확인
if second_min is not None:
    # 원본 배열에서 두 번째로 작은 숫자의 모든 인덱스 탐색
    positions = [i for i, x in enumerate(original_array) if x == second_min]

    # 두 번째로 작은 숫자가 하나만 있으면 그 위치를 출력
    if len(positions) == 1:
        print(positions[0] + 1)
    else:
        # 두 번쨰로 작은 숫자가 여러 개 있는 경우 -1 출력
        print(-1)
else:
    # 두 번째로 작은 숫자가 없는 경우 -1 출력
    print(-1)