def can_achieve_h(h, L, numbers):
    # 현재 H 점수를 만족하기 위해 필요한 원소 개수와 부족한 개수 계산
    greater_or_equal_h_count = sum(1 for num in numbers if num >= h)
    # 부족한 개수는 H 이상이 되도록 하려면 부족한 개수를 계산
    needed_to_increase = max(0, h - greater_or_equal_h_count)
    # 부족한 개수가 L 이하이면 가능
    return needed_to_increase <= L

def find_max_h(N, L, numbers):
    left, right = 0, 101  # H 점수는 0부터 100까지
    while left < right:
        mid = (left + right) // 2
        if can_achieve_h(mid, L, numbers):
            left = mid + 1
        else:
            right = mid
    return left - 1

# 입력 받기
N, L = map(int, input().split())
numbers = list(map(int, input().split()))

# 최대 H 점수 찾기
result = find_max_h(N, L, numbers)
print(result)