# 사람 수, 치즈 수, 치즈를 먹은 기록의 수, 아픈 기록의 수 입력 받기
N, M, D, S = map(int, input().split())

# 각 사람이 어떤 치즈를 언제 먹었는지 저장
people_eat_records = {i: [] for i in range(1, N + 1)}
for _ in range(D):
    p, m, t = map(int, input().split())
    people_eat_records[p].append((m, t))

# 아픈 사람과 그 시간을 저장
sick_records = {i: 101 for i in range(1, N + 1)}    # 초기값은 아픈 적이 없는 것으로 설정
for _ in range(S):
    p, t = map(int, input().split())
    sick_records[p] = t

# 상한 치즈 후보를 확인
bad_cheese_candidates = set(range(1, M + 1))

for person, sick_time in sick_records.items():
    # 아픈 사람이 먹었던 치즈 중, 아픈 시간 이전에 먹은 치즈만 후보에 포함
    valid_cheese = {m for m, t in people_eat_records[person] if t < sick_time}
    bad_cheese_candidates &= valid_cheese   # 교집합으로 후보 갱신

# 후보 중 하나라도 먹은 사람을 카운트
potential_sick = set()

for cheese in bad_cheese_candidates:
    for person, records in people_eat_records.items():
        for m, t in records:
            if m == cheese and t < sick_records[person]:
                potential_sick.add(person)

# 가능한 아픈 사람들의 수를 출력
print(len(potential_sick))