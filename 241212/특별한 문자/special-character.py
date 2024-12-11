from collections import Counter

def find_first_unique_char(s):
    """
    단 한 번만 등장하는 첫 번째 문자를 찾는 함수.

    Args:
    s (str): 입력 문자열 (소문자 알파벳으로만 구성).

    Returns:
    str or None: 단 한 번만 등장하는 첫 번째 문자, 없으면 None.
    """
    # Step 1: 문자열 내 모든 문자의 빈도 계산
    char_count = Counter(s)
    # Counter는 각 문자의 등장 횟수를 딕셔너리 형태로 저장합니다.

    # Step 2: 문자열을 순회하며 단 한 번 등장하는 문자 탐색
    for char in s:
        # 첫 번째로 빈도 1인 문자를 반환
        if char_count[char] == 1:
            return char

    # Step 3: 조건에 맞는 문자가 없으면 None 반환
    return None

# 사용자 입력 처리 및 결과 출력
if __name__ == "__main__":
    # 사용자 입력 받기
    input_string = input().strip()
    
    # 결과 계산
    result = find_first_unique_char(input_string)
    
    # 결과 출력
    if result is not None:
        print(result)
    else:
        print("None")