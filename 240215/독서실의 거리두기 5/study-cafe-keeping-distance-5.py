# 입력 받기
N = int(input())  # 좌석의 개수 N
seats = input()   # 좌석 상태를 나타내는 문자열

# 가장 가까운 두 사람의 거리의 최댓값을 저장할 변수
max_distance = 0
# 현재 사람을 앉히면서 확인하는 공석의 개수
current_distance = 0

# 좌석 상태를 순회하며 최대 거리 계산
for seat in seats:
    # 공석인 경우
    if seat == '0':
        # 현재 공석의 개수 증가
        current_distance += 1
    # 사람이 앉은 경우
    else:
        # 최대 거리 업데이트
        max_distance = max(max_distance, current_distance)
        # 현재 공석 개수 초기화
        current_distance = 0

# 마지막 좌석까지의 거리를 고려하여 최대 거리 업데이트
max_distance = max(max_distance, current_distance)

# 최대 거리 출력
print((max_distance + 1) // 2)