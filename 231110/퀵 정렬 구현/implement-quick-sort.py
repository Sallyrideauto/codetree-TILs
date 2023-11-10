'''
퀵 정렬(Quick Sort)은 평균적으로 O(n log n)의 시간 복잡도를 가지는 효율적인 정렬 알고리즘입니다. 
퀵 정렬의 기본 아이디어는 분할 정복(divide and conquer) 방식을 사용하는 것으로, 다음과 같은 단계를 거칩니다:
1. 분할(Divide): 배열을 두 부분으로 나눕니다. 
   이때, '피벗(pivot)'이라고 불리는 기준 값을 사용하여, 피벗보다 작은 모든 요소는 피벗의 왼쪽으로, 큰 모든 요소는 오른쪽으로 이동합니다.
2. 정복(Conquer): 피벗을 기준으로 나눈 두 부분 배열에 대해 재귀적으로 퀵 정렬을 수행합니다.
3. 결합(Combine): 정렬된 부분 배열들을 결합합니다. 퀵 정렬의 경우, 추가적인 결합 과정은 필요하지 않습니다.
'''

def quick_sort(arr, low, high):
    if low < high:
        # 파티션 과정을 거쳐 피벗을 기준으로 배열을 분할
        pivot_index = partition(arr, low, high)
        # 왼쪽 부분 배열 정렬
        quick_sort(arr, low, pivot_index - 1)
        # 오른쪽 부분 배열 정렬
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high] # 피벗은 배열의 마지막 요소
    i = low - 1 # i는 피벗보다 작은 요소들의 끝 인덱스

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # 피벗을 올바른 위치로 이동
    return i + 1    # 피벗의 인덱스 변환

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, n - 1)
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()