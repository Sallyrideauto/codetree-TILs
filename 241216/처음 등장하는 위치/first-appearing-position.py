# 입력 받기
n = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트

# 처음 등장 위치를 기록할 딕셔너리
first_position = {}

# 각 숫자의 첫 등장 위치 기록
for idx, num in enumerate(numbers):
    if num not in first_position:
        first_position[num] = idx + 1  # 위치는 1부터 시작

# 중복 제거된 숫자들을 정렬
sorted_numbers = sorted(first_position.keys())

# 결과 출력
for num in sorted_numbers:
    print(num, first_position[num])