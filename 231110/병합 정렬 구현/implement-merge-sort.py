'''
수행 시간과 메모리 사용량이 초과한 원인은 주로 병합 정렬 알고리즘의 구현 방식과 관련이 있습니다. 
제공된 구현에서는 리스트를 복사하고, 병합할 때 새로운 리스트를 생성하는 방식을 사용하고 있습니다. 
이러한 접근 방식은 메모리 사용량을 증가시키고, 추가적인 시간도 소모합니다.

해결 방안 중 하나는 병합 정렬을 좀 더 메모리 효율적으로 구현하는 것입니다. 이를 위해 다음과 같은 접근 방법을 사용할 수 있습니다:

1. 원본 리스트를 직접 변경
   병합 과정에서 새로운 리스트를 생성하는 대신, 원본 리스트에 정렬된 요소를 직접 복사합니다.
   이렇게 하면 병합 과정에서 발생하는 추가적인 메모리 할당을 줄일 수 있습니다.
2. 병합에 사용되는 임시 리스트 최적화
   병합 과정에서 사용되는 임시 리스트의 크기를 최소화하고 재사용하여 메모리 사용량을 줄입니다.

이 코드는 원본 배열 arr을 직접 수정하며, 정렬된 요소들을 임시 배열 temp에 저장한 후 arr에 다시 복사합니다.
이러한 방식은 추가적인 메모리 할당을 줄이고, 재귀 호출을 최적화하여 전체적인 성능을 향상시킵니다.
'''

def merge_sort(arr, temp, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, temp, start, mid)
        merge_sort(arr, temp, mid, end)
        merge(arr, temp, start, mid, end)

def merge(arr, temp, start, mid, end):
    i, j, k = start, mid, start

    while i < mid and j < end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j < end:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(start, end):
        arr[i] = temp[i]

# 메인 함수
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * n

    merge_sort(arr, temp, 0, n)
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()