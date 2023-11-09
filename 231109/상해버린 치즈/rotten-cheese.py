'''
이 문제를 해결하기 위한 방법을 단계별로 설명하겠습니다. 
우리는 이 정보를 사용하여 상한 치즈를 먹고 아플 가능성이 있는 최대 인원 수를 추정해야 합니다.

1. 각 치즈마다 먹은 시간을 추적하며, 각 사람이 아프기 시작한 정확한 시간을 기록합니다.
2. 아픈 기록으로부터 역추적하여, 해당 시간 이전에 먹은 치즈들 중 어느 것이 상한 치즈일 가능성이 있는지 파악합니다.
3. 아픈 사람이 먹은 치즈를 먹은 다른 모든 사람들도 아플 가능성이 있다고 간주합니다.
4. 모든 아픈 사람의 기록에 대해 이러한 과정을 반복하여, 상한 치즈를 먹었을 가능성이 있는 모든 사람들의 목록을 만듭니다.
5. 이 목록에 있는 사람 수가 필요한 약의 최대 개수가 됩니다.
'''

# 입력 받기
N, M, D, S = map(int, input().split())
cheese_logs = [list(map(int, input().split())) for _ in range(D)]
sick_logs = [list(map(int, input().split())) for _ in range(S)]

# 각 치즈를 누가 언제 먹었는지 저장하는 딕셔너리를 초기화합니다.
cheese_eaten = {m: [] for m in range(1, M+1)}

# 치즈 먹은 기록을 저장합니다.
for log in cheese_logs:
    p, m, t = log
    cheese_eaten[m].append((p, t))

# 상한 치즈를 먹었을 가능성이 있는 사람들의 집합입니다.
possible_sick_people = set()

# 아픈 기록을 통해 상한 치즈를 역추적합니다.
for log in sick_logs:
    p, t = log
    # 해당 사람이 아픈 시간 이전에 먹은 모든 치즈를 확인합니다.
    for m, eaten_times in cheese_eaten.items():
        for e_p, e_t in eaten_times:
            # 아픈 사람이 먹은 시간과 치즈를 먹은 시간을 비교합니다.
            if e_p == p and e_t < t:
                # 이 치즈를 먹은 다른 모든 사람도 상한 치즈를 먹었을 가능성이 있습니다.
                for other_p, _ in eaten_times:
                    possible_sick_people.add(other_p)

# 필요한 약의 최대 개수를 출력합니다.
print(len(possible_sick_people))