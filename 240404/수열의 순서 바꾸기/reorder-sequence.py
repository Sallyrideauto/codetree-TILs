def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    
    sorted_numbers = sorted(numbers)
    count = 1
    
    # 각 숫자의 정렬된 위치와 현재 위치의 차이를 계산하여 이동이 필요한지 확인합니다.
    for i in range(n):
        if numbers[i] != sorted_numbers[i]:
            count += 1
            
    print(count)

if __name__ == '__main__':
    main()