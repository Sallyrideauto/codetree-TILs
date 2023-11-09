'''
이 문제를 해결하기 위해서는 입력으로 주어진 범위 내에서 가능한 x의 최소값과 최대값을 각 단계마다 추적해야 합니다. 
각 단계에서 2를 곱할 때마다 가능한 x의 범위는 좁혀지게 되고, 이 범위는 다음 단계에서의 범위 결정에 영향을 미칩니다.

프로그램을 작성할 때 다음과 같은 로직을 따릅니다:
1. 범위를 나타내는 변수 두 개를 사용하여, 현재 가능한 x의 최소값(min_x)과 최대값(max_x)을 추적합니다. 
   초기값은 각각 float('inf')와 -float('inf')로 설정합니다.
2. 각 단계에서 a_i, b_i를 읽은 후, min_x는 max(min_x, a_i/2)로, max_x는 min(max_x, b_i/2)로 갱신합니다.
   여기서 2로 나누는 이유는 x에 2를 곱하기 전의 값이 필요하기 때문입니다.
3. 모든 단계를 완료한 후 min_x가 max_x보다 크면, 조건을 만족하는 x가 없다는 의미입니다.
   그러나 문제에서 가능한 x가 없는 입력은 주어지지 않는다고 가정했으므로, 이 경우는 고려하지 않아도 됩니다.
4. 최종적으로 min_x 값을 출력합니다. 이 값은 최소한의 시작 x 값을 의미하며, 모든 조건을 만족합니다.
'''

# 가능한 최솟값 x를 찾는 함수
def find_minimum_x(n, ranges):
    # 초기 가능한 x 값의 범위
    min_x = -float('inf')
    max_x = float('inf')
    
    # 각 단계별로 주어진 범위에 맞게 x의 범위를 조정
    for a, b in ranges:
        min_x = max(min_x, (a + 1) // 2)  # a_i/2의 올림값이 x의 최소 범위가 됨
        max_x = min(max_x, b // 2)        # b_i/2의 내림값이 x의 최대 범위가 됨
        
        # 현재 단계에서 가능한 x의 범위가 없으면 break (문제 조건상 이 경우는 없다고 가정)
        if min_x > max_x:
            break
    
    # 가능한 x 값 중 최솟값 반환
    return min_x

# 입력 받기
n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

# 가능한 최소 x 값을 찾아 출력
print(find_minimum_x(n, ranges))