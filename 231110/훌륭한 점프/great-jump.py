'''
문제를 해결하기 위해 다른 접근 방법을 사용해야 할 것 같습니다.
이 문제는 ‘슬라이딩 윈도우’ 방식으로 해결할 수 있습니다.
이 방식은 각 구간 내에서 최댓값과 최솟값의 차이를 계산하여, 이 차이가 조건을 만족하는 최대 구간의 크기를 찾는 데 사용됩니다.

문제의 요구 사항에 따라, 우리는 각 돌을 건너뛰며 이동할 때 거쳐간 돌들 중 최댓값이 최소가 되도록 해야 합니다. 
이를 위해 다음과 같은 접근 방식을 사용할 수 있습니다:

1. 각 돌 사이의 가능한 거리를 계산합니다.
2. 이 거리들 중 최댓값을 최소화하는 구간을 찾습니다.
3. 이 구간의 크기가 최대가 되도록 합니다.

이 코드는 가능한 모든 거리를 계산한 후 이를 내림차순으로 정렬하고, k번째로 큰 거리를 최소 최대 거리로 선택합니다. 
이것은 k번째 점프에서 가능한 최대 거리를 최소화하는 것과 같습니다.
'''

n, k = map(int, input().split())
stones = list(map(int, input().split()))

def min_max_distance(stones, k):
    # 거리들을 저장할 리스트
    distances = []
    for i in range(n - 1):
        for j in range(i + 1, min(i + k + 1, n)):
            # 각 돌 사이의 가능한 거리 계산
            distances.append(stones[j] - stones[i])

    # 최소 최대 거리 탐색
    distances.sort(reverse = True)
    return distances[k - 1]

print(min_max_distance(stones, k))