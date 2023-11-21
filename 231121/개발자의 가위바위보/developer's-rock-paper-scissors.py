from itertools import permutations

def calculate_wins(mappings, games):
    # 첫 번째 개발자의 승리 횟수를 계산하는 함수
    wins = 0
    for game in games:
        if mappings[game[0]] == '가위' and mappings[game[1]] == '보':
            wins += 1
        elif mappings[game[0]] == '바위' and mappings[game[1]] == '가위':
            wins += 1
        elif mappings[game[0]] == '보' and mappings[game[1]] == '바위':
            wins += 1
    return wins

def max_wins(N, games):
    # 모든 순열에 대해 승리 횟수를 계산하고 최댓값을 찾는 함수
    max_wins = 0
    for perm in permutations(['가위', '바위', '보']):
        # 숫자 1, 2, 3에 가위바위보 매칭
        mappings = {1: perm[0], 2: perm[1], 3: perm[2]}
        max_wins = max(max_wins, calculate_wins(mappings, games))
    return max_wins

N = int(input())
games = [list(map(int, input().split())) for i in range(N)]

print(max_wins(N, games))