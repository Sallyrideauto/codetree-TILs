def find_ABCD(inputs):
    inputs = set(inputs)    # 입력값을 세트로 변환
    for A in range(1, 41):
        for B in range(1, 41):
            for C in range(1, 41):
                for D in range(1, 41):
                    # 모든 조합 및 합산 계산
                    sums = {
                        A, B, C, D, 
                        A + B, B + C, C + D, 
                        D + A, A + C, B + D, 
                        A + B + C, A + B + D, 
                        A + C + D, B + C + D, 
                        A + B + C + D
                    }
                    if sums == inputs:  # 입력 세트와 계산된 세트가 같다면
                        return (A, B, C, D)

lst = list(map(int, input().split()))
result = find_ABCD(lst)
print(*result)  # 튜플의 원소를 공백으로 구분하여 출력