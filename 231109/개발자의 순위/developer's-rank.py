'''
이 문제를 해결하기 위해서는 각 개발자 간의 순위를 비교하는 모든 가능한 쌍을 조사해야 합니다. 
각 경기마다 주어진 순위를 바탕으로 a번 개발자가 b번 개발자보다 항상 높은 순위를 기록했는지 확인합니다.

이 코드는 다음과 같은 로직을 따릅니다:
1. K와 N을 입력받아 순위 데이터를 저장합니다.
2. 모든 가능한 (a, b) 쌍에 대해 always_higher 함수를 사용하여 a가 b보다 항상 순위가 높은지 확인합니다.
3. 조건을 만족하는 쌍의 수를 세어 결과를 출력합니다.

always_higher 함수는 주어진 모든 경기(rankings)에서 a가 b보다 먼저 나타나는지 확인합니다. 
이를 위해 리스트의 index 메소드를 사용하여 b의 인덱스 이전에 a가 있는지 검사합니다. 
모든 경기에서 이 조건이 참이면 함수는 True를 반환합니다.
'''

K, N = map(int, input().split())
rankings = [list(map(int, input().split())) for _ in range(K)]

# (a, b) 쌍이 항상 a가 b보다 높은 순위인지 체크하는 함수
def always_higher(rankings, a, b):
    return all(a in r[:r.index(b)] for r in rankings)

# 모든 가능한 (a, b) 쌍에 대해 체크
count = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a != b and always_higher(rankings, a, b):
            count += 1

print(count)