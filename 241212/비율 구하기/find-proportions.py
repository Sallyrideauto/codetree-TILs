# Step 1: 필요한 모듈 가져오기
from collections import defaultdict

# Step 2: 입력 받기
n = int(input())  # 문자열의 개수
strings = [input().strip() for _ in range(n)]  # 각 문자열 입력받기

# Step 3: 문자열 빈도 계산
frequency = defaultdict(int)  # 딕셔너리 초기화
for string in strings:
    frequency[string] += 1  # 문자열 등장 횟수 증가

# Step 4: 전체 문자열 개수와 빈도 비율 계산
total_strings = len(strings)  # 전체 문자열 개수
results = []  # 결과 저장 리스트
for string, count in frequency.items():
    percentage = (count / total_strings) * 100  # 비율 계산
    results.append((string, percentage))  # 튜플 형태로 저장

# Step 5: 사전순 정렬
results.sort(key=lambda x: x[0])  # 문자열 기준 사전순 정렬

# Step 6: 출력 형식에 맞게 결과 출력
for string, percentage in results:
    print(f"{string} {percentage:.4f}")  # 소수점 4째 자리까지 출력
