def heapify(arr, n, i):
    # 가장 큰 요소를 루트로 설정
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 자식이 현재 요소보다 크면 위치 변경
    if left < n and arr[largest] < arr[left]:
        largest = left

    # 오른쪽 자식이 현재 요소보다 크면 위치 변경
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 루트가 변경되었다면, 계속해서 하위 트리에 대해 힙을 구축
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 힙 구축
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 추출하면서 힙 정렬 수행
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # 루트(최대값)를 배열의 끝으로 이동
        heapify(arr, i, 0)  # 힙의 크기 줄이기

# 메인 함수
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    heap_sort(arr)
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()