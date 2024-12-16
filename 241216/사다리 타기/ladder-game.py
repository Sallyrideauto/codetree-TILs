from itertools import combinations
import copy

def simulate_ladder(n, ladder):
    """
    주어진 사다리 상태에서 각 시작점에서 최종 결과를 반환하는 함수
    """
    result = list(range(1, n + 1))  # 1부터 n까지 출발점
    for a, b in sorted(ladder, key=lambda x: x[1]):  # 가로줄 y값 기준으로 정렬
        if 0 <= a - 1 < n - 1:  # 인덱스 범위 확인
            result[a - 1], result[a] = result[a], result[a - 1]  # 가로줄에서 위치 교환
    return result

def find_min_ladders(n, m, ladders):
    """
    주어진 사다리 상태에서 동일한 결과를 얻기 위한 최소 가로줄 수를 찾는 함수
    """
    # 초기 사다리 결과
    original_result = simulate_ladder(n, ladders)
    min_ladders = m  # 초기 최소 가로줄 수는 모든 가로줄 사용

    # 1개부터 m개까지 가로줄 조합을 시도
    for r in range(m + 1):
        for subset in combinations(ladders, r):  # r개 가로줄 조합
            if simulate_ladder(n, subset) == original_result:  # 동일 결과 확인
                min_ladders = min(min_ladders, r)  # 최소 가로줄 수 업데이트
                break
        if min_ladders == r:  # 더 작은 r로 만족했으면 탈출
            break

    return min_ladders

# 입력 처리
n, m = map(int, input().split())
ladders = [tuple(map(int, input().split())) for _ in range(m)]

# 최소 가로줄 수 찾기
result = find_min_ladders(n, m, ladders)
print(result)
