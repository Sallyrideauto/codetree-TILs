def remove_blocks(blocks, s, e):
    # s와 e 범위에 해당하는 블럭을 제거하고 나머지 블럭 반환
    return blocks[:s-1] + blocks[e:]

def main():
    # 입력 처리
    n = int(input())
    blocks = [int(input()) for _ in range(n)]

    s1, e1 = map(int, input().split())
    s2, e2 = map(int, input().split())

    # 첫 번째 제거 작업
    blocks = remove_blocks(blocks, s1, e1)
    # 두 번째 제거 작업
    blocks = remove_blocks(blocks, s2, e2)

    # 결과 출력
    print(len(blocks))
    for block in blocks:
        print(block)

if __name__ == "__main__":
    main()