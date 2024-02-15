# 입력 받기
N = int(input())  # 좌석의 개수 N
seats = input()   # 좌석 상태를 나타내는 문자열

# 가장 가까운 두 사람의 거리의 최댓값을 저장할 변수
max_distance = 0
# 사람이 앉을 수 있는 시작 인덱스를 저장할 변수
start_index = 0

# 좌석 상태를 순회하며 최대 거리 계산
for i in range(N):
    # 사람이 앉지 않은 경우
    if seats[i] == '0':
        # 시작 인덱스가 설정되지 않은 경우, 시작 인덱스를 설정
        if start_index == 0:
            start_index = i
    # 사람이 앉은 경우
    else:
        # 시작 인덱스가 설정되어 있을 때, 최대 거리 갱신
        if start_index != 0:
            max_distance = max(max_distance, (i - start_index) // 2)
            start_index = 0

# 마지막 좌석까지의 거리를 고려하여 최대 거리 업데이트
if start_index != 0:
    max_distance = max(max_distance, N - 1 - start_index) + 1

# 최대 거리 출력
print(max_distance)