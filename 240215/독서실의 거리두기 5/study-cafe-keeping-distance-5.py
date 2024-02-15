N = int(input()) # 죄석의 개수 N
seats = input()  # 좌석 상태를 나타내는 문자열

# 최대 거리를 저장하는 변수
max_distance = 0
current_distance = 0

# 현재 좌석 상태를 순회하면서 최대 거리 계산
for seat in seats:
    if seat == '0':
        current_distance += 1
    else:
        # 만약 현재 거리가 최대 거리보다 크다면 최대 거리를 업데이트
        max_distance = max(max_distance, (current_distance + 1) // 2)
        current_distance = 0

# 마지막 좌석까지의 거리를 최대 거리로 갱신
max_distance = max(max_distance, current_distance)

# 최대 거리 출력
print(max_distance)