def cnt_sequence(n, m, sequence, queries):
    cnt_dict = {}   # 각 숫자의 등장 횟수를 저장할 딕셔너리
    # 수열의 숫자들을 순회하며 딕셔너리를 채우기
    for num in sequence:
        if num in cnt_dict:
            cnt_dict[num] += 1
        else:
            cnt_dict[num] = 1
    
    results = []    # 결과를 저장할 리스트
    # 주어진 질의에 대해 각 숫자가 몇 번 등장했는지 결과에 추가
    for query in queries:
        # 딕셔너리에 해당 숫자가 있으면 그 값을, 없으면 0을 추가
        results.append(cnt_dict.get(query, 0))

    return results

n, m = map(int, input().split())
sequence = list(map(int, input().split()))
queries = list(map(int, input().split()))

results = cnt_sequence(n, m, sequence, queries)
print(" ".join(map(str, results)))