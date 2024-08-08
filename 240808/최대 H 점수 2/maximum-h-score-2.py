def can_achieve_h(h, L, numbers):
    # H 이상의 원소 개수를 계산
    count_h_or_more = sum(1 for num in numbers if num >= h)
    
    # 부족한 개수 계산
    needed_to_increase = max(0, h - count_h_or_more)
    
    # 부족한 개수가 L 이하이면 가능
    return needed_to_increase <= L

def find_max_h(N, L, numbers):
    max_H = 0
    # H 점수를 0부터 100까지 검사
    for h in range(101):
        if can_achieve_h(h, L, numbers):
            max_H = h
    return max_H

# 입력 받기
N, L = map(int, input().split())
numbers = list(map(int, input().split()))

# 최대 H 점수 찾기
result = find_max_h(N, L, numbers)
print(result)