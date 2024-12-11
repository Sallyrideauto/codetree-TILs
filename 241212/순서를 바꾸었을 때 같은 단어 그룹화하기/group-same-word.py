from collections import Counter

def max_group_size(n, words):
    """
    n: 단어의 개수
    words: 단어 리스트
    """
    # 1. 각 단어를 알파벳 순으로 정렬하여 그룹화
    sorted_words = [''.join(sorted(word)) for word in words]
    
    # 2. 그룹별 단어 개수를 계산
    word_groups = Counter(sorted_words)
    
    # 3. 가장 큰 그룹의 크기를 반환
    return max(word_groups.values())

# 입력 처리
if __name__ == "__main__":
    # 첫 번째 줄: 단어의 개수
    n = int(input().strip())
    
    # 두 번째 줄부터: 각 단어 입력
    words = [input().strip() for _ in range(n)]
    
    # 결과 출력
    print(max_group_size(n, words))
