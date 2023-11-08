n, m = map(int, input().split())

# 각 쌍의 출현 횟수를 기록하기 위한 딕셔너리
pair_count = {}

# 가장 많이 출현한 쌍의 횟수를 기록할 변수
max_count = 0

# m번의 입력에 대해 처리
for _ in range(m):
    a, b = map(int, input().split())

    # (a, b)와 (b, a)를 같은 쌍으로 취급
    if a > b:
        a, b = b, a # a가 항상 b보다 작거나 같도록 조정
    
    # 딕셔너리에 쌍의 출현 횟수를 업데이트
    if (a, b) in pair_count:
        pair_count[(a, b)] += 1
    else:
        pair_count[(a, b)] = 1

    # 최대 출현 횟수 업데이트
    max_count = max(max_count, pair_count[(a, b)])

# 가장 많이 출현한 쌍의 횟수 출력
print(max_count)