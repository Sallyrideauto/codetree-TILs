from collections import Counter

def top_k_frequent_numbers(n, k, numbers):
    # 빈도수를 계산하기 위해 Counter 사용
    count = Counter(numbers)
    
    # 등장 횟수 내림차순, 숫자 크기 내림차순으로 정렬
    sorted_numbers = sorted(count.keys(), key=lambda x: (-count[x], -x))
    
    # 상위 k개의 숫자를 출력
    result = sorted_numbers[:k]
    print(" ".join(map(str, result)))

# 입력 받기
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# 함수 호출
top_k_frequent_numbers(n, k, numbers)