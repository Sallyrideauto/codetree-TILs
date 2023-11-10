'''
이 문제를 해결하기 위해서는 주어진 숫자들을 정렬한 뒤, 
각 숫자를 시작점으로 하여 최댓값과 최솟값의 차이가 K 이하가 되는 범위 내에서 최대한 많은 숫자를 포함하는 부분 배열을 찾아야 합니다.

이 코드는 두 포인터(start, end)를 사용하여 부분 배열을 슬라이딩 윈도우 방식으로 탐색합니다. 
각 원소를 시작점으로 하여 최댓값과 최솟값의 차이가 K 이하가 될 때까지 끝점(end)을 오른쪽으로 이동시키고, 
차이가 K보다 커지면 시작점(start)을 오른쪽으로 이동시키면서 최대 개수를 찾습니다.
'''

def max_numbers_within_k(arr, K):
    # 주어진 배열을 정렬
    arr.sort()
    max_count = 0
    start = 0

    # 배열을 순회하면서 각 원소를 시작점으로 하는 최대 개수 탐색
    for end in range(N):
        # 현재 end 인덱스에 있는 원소와 start 인덱스에 있는 원소의 차이가 K 이하인 동안
        while arr[end] - arr[start] > K:
            # start를 오른쪽으로 이동
            start += 1
        # 현재 부분 배열의 크기(최대 개수)를 계산
        max_count = max(max_count, end - start + 1)

    return max_count

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 뽑을 수 있는 원소의 최대 개수를 출력
print(max_numbers_within_k(arr, K))