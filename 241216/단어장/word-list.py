# 알고리즘 설명
# 1. 입력 데이터를 읽어옵니다. 첫 번째 줄은 단어의 개수 n이고, 그 다음 줄부터는 n개의 단어입니다.
# 2. 각 단어의 등장 횟수를 계산하기 위해 `collections.Counter`를 사용합니다.
#    이는 해시 테이블 기반의 자료구조로, 각 단어의 등장 횟수를 효율적으로 계산합니다.
# 3. 사전순으로 정렬된 단어와 해당 단어의 등장 횟수를 출력합니다.

# 구현
from collections import Counter

# 입력 받기
n = int(input())  # 첫 번째 줄에서 단어의 개수를 입력받음
words = [input().strip() for _ in range(n)]  # n개의 단어를 리스트로 입력받음

# 단어 빈도수 계산
word_count = Counter(words)  # 각 단어의 빈도를 계산함

# 사전순 정렬
sorted_word_count = sorted(word_count.items())  # 단어를 사전순으로 정렬함

# 결과 출력
for word, count in sorted_word_count:
    print(word, count)
