def rotate_triangle_belt(n, t, left_top, right_top, bottom):
    for _ in range(t):
        # 각 변의 마지막 숫자를 저장
        last_left_top = left_top[-1]
        last_right_top = right_top[-1]
        last_bottom = bottom[-1]

        # 시계 방향으로 숫자 이동
        # 왼쪽 위 -> 오른쪽 위, 오른쪽 위 -> 아래, 아래 -> 왼쪽 위
        left_top = [last_bottom] + left_top[:-1]
        right_top = [last_left_top] + right_top[:-1]
        bottom = [last_right_top] + bottom[:-1]

    # 결과 출력
    print(" ".join(map(str, left_top)))
    print(" ".join(map(str, right_top)))
    print(" ".join(map(str, bottom)))

n, t = map(int, input().split())
left_top = list(map(int, input().split()))
right_top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

rotate_triangle_belt(n, t, left_top, right_top, bottom)