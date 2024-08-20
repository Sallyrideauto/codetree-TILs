def rotate_conveyor_belt(n, t, top_row, bottom_row):
    # t초 동안 회전시키기
    for _ in range(t):
        last_top = top_row[-1]  # 위쪽 마지막 숫자 저장
        last_bottom = bottom_row[-1]    # 아래쪽 마지막 숫자 저장

        # 아래쪽 숫자들을 오른쪽으로 한 칸씩 이동
        bottom_row = [last_top] + bottom_row[:-1]

        # 위쪽 숫자들을 왼쪽으로 한 칸씩 이동
        top_row = top_row[:-1]
        top_row = [last_bottom] + top_row


    # 결과 출력
    print(" ".join(map(str, top_row)))
    print(" ".join(map(str, bottom_row)))

n, t = map(int, input().split())
top_row = list(map(int, input().split()))
bottom_row = list(map(int, input().split()))

rotate_conveyor_belt(n, t, top_row, bottom_row)