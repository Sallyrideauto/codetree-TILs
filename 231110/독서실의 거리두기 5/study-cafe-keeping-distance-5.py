def max_distance(seats):
    # 앉아 있는 사람들 사이의 거리를 찾습니다.
    prev = -1
    max_gap = 0
    n = len(seats)
    
    for i, seat in enumerate(seats):
        if seat == '1':
            if prev == -1:
                # 첫 번째 사람까지의 거리
                max_gap = i
            else:
                # 중간 사람들의 거리의 절반값
                max_gap = max(max_gap, (i - prev) // 2)
            prev = i
    
    # 마지막 사람부터 끝까지의 거리
    max_gap = max(max_gap, n - 1 - prev)

    return max_gap

# 입력 받기
N = int(input())
seats = input().strip()

# 최대 거리 출력
print(max_distance(seats))