'''
문제를 다시 파악해보면, 우리는 각 사람이 아프기 시작한 시간 바로 전에 먹은 치즈들 중에 상한 치즈가 있을 것입니다. 
이 상한 치즈를 먹은 모든 사람들은 약을 필요로 할 것입니다. 
상한 치즈를 식별하기 위해서는 다음 단계를 따라야 합니다:

1. 아픈 기록이 있는 각 사람에 대해, 그들이 아픈 것으로 기록된 시간 바로 전에 먹은 치즈들을 찾습니다.
2. 찾아낸 치즈들의 교집합을 구합니다. 이 교집합에 포함된 치즈가 상한 치즈일 가능성이 높습니다.
3. 상한 치즈일 가능성이 있는 치즈를 먹은 모든 사람들을 찾습니다.
4. 그 사람들의 수를 세어 약이 필요한 최대 개수를 계산합니다.
'''

N, M, D, S = map(int, input().split())
cheese_logs = [set() for _ in range(M+1)]  # 각 치즈마다 누가 언제 먹었는지 기록합니다.
sick_logs = []  # 아픈 기록을 저장합니다.

# 치즈를 먹은 기록을 저장합니다.
for _ in range(D):
    p, m, t = map(int, input().split())
    cheese_logs[m].add((p, t))

# 아픈 사람의 기록을 저장합니다.
for _ in range(S):
    p, t = map(int, input().split())
    sick_logs.append((p, t))

# 가능한 상한 치즈의 후보를 찾습니다.
possible_bad_cheeses = set(range(1, M+1))
for p, t in sick_logs:
    # 아픈 사람이 아프기 전에 먹은 치즈들을 확인합니다.
    cheeses_before_sick = set()
    for m in range(1, M+1):
        for person, time in cheese_logs[m]:
            if person == p and time < t:
                cheeses_before_sick.add(m)
                break
    # 상한 치즈 후보를 좁혀나갑니다.
    possible_bad_cheeses &= cheeses_before_sick

# 상한 치즈를 먹었을 가능성이 있는 사람들을 찾습니다.
possible_sick_people = set()
for m in possible_bad_cheeses:
    for p, t in cheese_logs[m]:
        possible_sick_people.add(p)

# 필요한 약의 최대 개수를 출력합니다.
print(len(possible_sick_people))