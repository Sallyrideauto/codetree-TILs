def minimum_relocations_to_sort(N, sequence):
    # LIS를 찾기 위한 DP 배열과 경로 복원을 위한 배열 초기화
    dp = [1] * N
    parent = list(range(N))
    
    # LIS 계산
    for i in range(1, N):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    # 최대 LIS 길이 계산
    max_LIS_length = max(dp)
    index = dp.index(max_LIS_length)
    
    # LIS 구성 요소 확인
    LIS_elements = set()
    while parent[index] != index:
        LIS_elements.add(sequence[index])
        index = parent[index]
    LIS_elements.add(sequence[index])
    
    # LIS를 제외한 원소들의 이동이 필요한 횟수 계산
    move_count = 0
    for num in sequence:
        if num not in LIS_elements:
            move_count += 1
    
    return move_count

# 입력 받기
N = int(input())
sequence = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = minimum_relocations_to_sort(N, sequence)
print(result)