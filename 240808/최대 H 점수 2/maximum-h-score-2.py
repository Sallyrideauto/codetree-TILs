def find_max_h(N, L, numbers):
    max_H = 0

    # H를 0부터 100까지 검사
    for h in range(101):
        # 현재 H 점수에 대해 필요한 개수를 계산
        count_h_or_more = sum(1 for num in numbers if num >= h)

        # 부족한 개수 계산
        needed_to_increase = max(0, h - count_h_or_more)

        # 부족한 개수 <= L이면 현재 H 점수가 가능한 경우
        if needed_to_increase <= L:
            max_H = h

    return max_H

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

result = find_max_h(N, L, numbers)
print(result)