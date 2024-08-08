def restore_sequence(N, sums):
    # 수열을 저장할 리스트
    result = [0] * N
    used = [False] * (N + 1)
    
    def backtrack(index):
        if index == N:
            return True
        
        # 현재 합에서 가능한 다음 수를 계산
        if index == 0:
            for first in range(1, N + 1):
                result[index] = first
                used[first] = True
                if backtrack(index + 1):
                    return True
                used[first] = False
        else:
            next_num = sums[index - 1] - result[index - 1]
            if 1 <= next_num <= N and not used[next_num]:
                result[index] = next_num
                used[next_num] = True
                if backtrack(index + 1):
                    return True
                used[next_num] = False
        
        return False
    
    backtrack(0)
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    sums = list(map(int, data[1:]))
    
    result = restore_sequence(N, sums)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()