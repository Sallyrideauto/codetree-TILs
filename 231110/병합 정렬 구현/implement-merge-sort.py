'''
병합 정렬(Merge Sort)은 분할 정복(divide and conquer) 방식을 사용하는 효율적인 정렬 알고리즘입니다. 
주어진 리스트를 반으로 나누고, 각 부분을 재귀적으로 정렬한 후, 두 부분을 병합하는 방식으로 작동합니다. 
이 알고리즘은 평균적으로 O(n log n)의 시간 복잡도를 가집니다.

병합 정렬을 구현하는 방법은 다음과 같습니다:

1. 리스트의 길이가 1 이하이면 이미 정렬된 것으로 간주하고 반환합니다.
2. 그렇지 않으면 리스트를 반으로 나누어 각각을 재귀적으로 정렬합니다.
3. 두 개의 정렬된 리스트를 병합하여 하나의 정렬된 리스트로 만듭니다.

이 프로그램은 merge_sort 함수를 사용하여 입력된 배열을 정렬합니다. 
merge_sort 함수는 배열을 두 부분으로 나누고, 각 부분을 재귀적으로 정렬한 다음, merge 함수를 사용하여 이 두 배열을 병합합니다. 
merge 함수는 두 정렬된 배열을 순서대로 비교하며 하나의 정렬된 배열로 만듭니다.
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # 왼쪽 반을 재귀적으로 정렬
    right = merge_sort(arr[mid:])   # 오른쪽 반을 재귀적으로 정렬

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 왼쪽과 오른쪽 배열을 순회하며 요소를 비교하여 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
        else:
            result.append(right[j])
            j += 1

    # 남은 요소들을 결과 배열에 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 메인 함수
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = merge_sort(arr)
    print(' '.join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()