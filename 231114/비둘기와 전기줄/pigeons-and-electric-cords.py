N = int(input())
walks = [list(map(int, input().split())) for _ in range(N)]

# 비둘기의 마지막 위치를 저장할 딕셔너리
last_positions = {}
cross_count = 0 # 비둘기가 도로를 건넨 횟수

# 입력된 관찰 데이터 순회
for pigeon_number, current_posiotion in walks:
    # 비둘기의 마지막 위치가 기록되어 있고, 현재 위치가 다른 경우
    if pigeon_number in last_positions and last_positions[pigeon_number] != current_posiotion:
        cross_count += 1    # 건넌 횟수 증가
    last_positions[pigeon_number] = current_posiotion   # 마지막 위치 업데이트

print(cross_count)