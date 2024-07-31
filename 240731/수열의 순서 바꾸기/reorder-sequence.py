N = int(input())
arr = list(map(int, input().split()))

# 현재 상태에서 정렬된 부분의 길이를 찾는 함수
def count_sorted_length(arr):
    length = 1
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            length += 1
        else:
            break
    return length

min_moves = N  # 초기 최소 이동 횟수는 최대값인 N으로 설정
current_arr = arr[:]

for i in range(N):
    # 현재 배열의 정렬된 부분 길이를 찾습니다.
    sorted_length = count_sorted_length(current_arr)
    
    # 현재 배열의 정렬된 부분을 제외한 나머지 부분을 뒤로 보내는 횟수를 계산합니다.
    moves = N - sorted_length
    min_moves = min(min_moves, moves)
    
    # 맨 앞의 원소를 뒤로 보냅니다.
    current_arr.append(current_arr.pop(0))

if min_moves == 1:
    print(moves)
else:
    print(min_moves)