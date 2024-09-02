def run_length_encoding(s):
    # Run-Length Encoding을 수행하는 함수
    if not s:
        return ""

    # 결과를 저장할 문자열
    encoded = ""
    # 현재 관찰중인 문자
    current_char = s[0]
    count = 0

    for char in s:
        if char == current_char:
            count += 1
        else:
            # 현재 문자와 그 개수를 결과에 추가
            encoded += current_char + str(count)
            current_char = char
            count = 1

    # 마지막 문자열 묶은 처리
    encoded += current_char + str(count)

    return len(encoded)

def minimum_encoded_length(s):
    # 모든 가능한 시프트에 대해 RLE 후 최소 길이를 구하는 함수
    n = len(s)
    min_length = float('inf')

    for i in range(n):
        # 오른쪽으로 i칸 시프트
        shifted_s = s[-i:] + s[:-i]
        # RLE 수행 후 길이 측정
        encoded_length = run_length_encoding(shifted_s)
        # 최소 길이 업데이트
        if encoded_length < min_length:
            min_length = encoded_length

    return min_length

input_string = input().strip()
print(minimum_encoded_length(input_string))