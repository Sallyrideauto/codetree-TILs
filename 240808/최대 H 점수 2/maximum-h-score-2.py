def can_achieve_h(h, L, numbers):
    # H 점수를 만족하기 위해 필요한 최소 개수 계산
    required_count = sum(1 for num in numbers if num >= h)
    # 부족한 개수 계산
    needed_to_increase = max(0, h - required_count)
    return needed_to_increase <= L

def find_max_h(N, L, numbers):
    left, right = 0, 101    # H 점수는 0부터 100까지
    while left < right:
        mid = (left + right) // 2
        if can_achieve_h(mid, L, numbers):
            left = mid + 1
        else:
            right = mid
    return left - 1

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

result = find_max_h(N, L, numbers)
print(result)