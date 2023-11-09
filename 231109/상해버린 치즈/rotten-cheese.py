# 입력을 받습니다.
N, M, D, S = map(int, input().split())
cheese_eaten = [[] for _ in range(M+1)]  # 치즈별로 먹은 사람과 시간을 저장할 리스트
sick_people = {}  # 아픈 시간과 그 시간에 해당하는 사람을 저장할 딕셔너리

# 치즈를 먹은 기록을 저장합니다.
for _ in range(D):
    p, m, t = map(int, input().split())
    cheese_eaten[m].append((t, p))  # 치즈 m을 시간 t에 사람 p가 먹었다.

# 각 치즈를 먹은 기록을 시간순으로 정렬합니다.
for m in range(1, M+1):
    cheese_eaten[m].sort()

# 아픈 사람의 기록을 저장합니다.
for _ in range(S):
    p, t = map(int, input().split())
    sick_people[p] = t

# 상한 치즈 추정을 위한 딕셔너리입니다.
# 사람이 먹은 치즈 중에서 아프기 전에 먹은 마지막 치즈를 상한 치즈라고 가정합니다.
suspected_bad_cheese = set()
for p, t in sick_people.items():
    last_eaten = -1
    for m in range(1, M+1):
        # 해당 사람이 먹은 각 치즈에 대해 아프기 전 마지막 치즈를 찾습니다.
        for cheese_time, cheese_person in cheese_eaten[m]:
            if cheese_person == p and cheese_time < t and cheese_time > last_eaten:
                last_eaten = cheese_time
                suspected_bad_cheese.add(m)

# 상한 치즈를 먹은 사람들을 찾습니다.
sick_after_eating = set()
for m in suspected_bad_cheese:
    for cheese_time, cheese_person in cheese_eaten[m]:
        # 상한 치즈를 먹었던 모든 사람을 찾습니다.
        sick_after_eating.add(cheese_person)

# 필요한 약의 최대 개수를 출력합니다.
print(len(sick_after_eating))