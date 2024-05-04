import itertools

def generate_pairs(K, N):
    # 1부터 K까지의 숫자들을 생성
    numbers = range(1, K + 1)
    # itertools.product를 사용하여 숫자들의 N번 반복에 대한 모든 조합을 생성
    results = itertools.product(numbers, repeat = N)
    # 결과를 출력
    for result in results:
        print(" ".join(map(str, result)))

def main():
    K, N = map(int, input().split())
    # 입력받은 K와 N을 이용하여 순서쌍 생성 및 출력
    generate_pairs(K, N)

if __name__ == "__main__":
    main()