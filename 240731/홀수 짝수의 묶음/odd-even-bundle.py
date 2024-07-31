def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = 0

    odd = 0
    even = 0

    for i in range(n):
        num = arr[i]
        if num % 2 != 0:
            odd += 1
        else:
            even += 1

    if even > odd:
        ans = odd * 2 + 1
    elif even == odd:
        ans = even + odd
    else:
        ans = even * 2
        size = odd - even

        if size % 3 == 0:
            ans += (size // 3) * 2
        else:
            if (size % 3) % 2 == 0:
                ans += (size // 3) * 2 + 1
            else:
                ans += (size // 3) * 2 - 1

    print(ans)

if __name__ == "__main__":
    main()