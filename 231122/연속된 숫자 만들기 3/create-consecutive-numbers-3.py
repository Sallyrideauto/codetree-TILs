'''
이 문제는 세 사람이 일렬로 서 있는 위치를 조정하여 그들이 연속된 숫자 위치에 서도록 최대 이동 횟수를 계산하는 것입니다. 
이를 위해 다음과 같은 접근 방법을 사용할 수 있습니다:
1. 세 위치 정렬: 먼저, 세 위치를 정렬하여 순서대로 배열합니다. 이렇게 하면 각 사람이 위치한 곳을 쉽게 파악할 수 있습니다.
2. 이동 횟수 계산: 연속된 숫자 위치를 만들기 위해 가장 왼쪽 또는 오른쪽에 있는 사람을 중간 사람의 양쪽으로 이동시키는 것이 핵심입니다.
   이를 위해 두 가지 주요 이동을 고려합니다:
	• 왼쪽 사람을 중간 또는 중간 사람의 바로 오른쪽으로 이동시킵니다.
	• 오른쪽 사람을 중간 또는 중간 사람의 바로 왼쪽으로 이동시킵니다.
3. 최대 이동 횟수 계산: 각 단계에서의 이동 횟수를 계산하고, 이 중 최대 이동 횟수를 찾습니다.
'''

def max_moves_to_consecutive(a, b, c):
    # 세 위치를 정렬
    positions = sorted([a, b, c])

    # 이동 횟수 계산
    moves = 0
    while True:
        # 이미 연속된 숫자 위치인 경우
        if positions[2] - positions[0] == 2:
            break
        
        # 왼쪽 사람 이동
        if positions[1] - positions[0] > 1:
            positions[0] += 2
            moves += 1

        # 추가 이동 없이 연속된 숫가 위치에 도달한 경우
        if positions[2] - positions[0] == 2:
            break

    return moves

a, b, c = map(int, input().split())
print(max_moves_to_consecutive(a, b, c))