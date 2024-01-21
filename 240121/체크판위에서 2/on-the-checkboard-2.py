def count_valid_paths(R, C, grid):
    def is_valid_jump(r1, c1, r2, c2):
        # 점프가 가능한지 확인 (오른쪽 및 아래로 이동)
        return r1 < r2 and c1 < c2 and grid[r1][c1] != grid[r2][c2]
    
    valid_paths = 0
    # 모든 가능한 중간 점 지점 쌍에 대해 검사
    for r1 in range(R-1):
        for c1 in range(C-1):
            for r2 in range(r1+1, R):
                for c2 in range(c1+1, C):
                    # 첫 번째 점프가 유효한 경우
                    if is_valid_jump(0, 0, r1, c1) and is_valid_jump(r1, c1, r2, c2) and is_valid_jump(r2, c2, R-1, C-1):
                        valid_paths += 1
    return valid_paths

# 입력 예제
R, C = map(int, input().split())
grid = [input().split() for i in range(R)]

# 함수 호출 및 결과 출력
print(count_valid_paths(R, C, grid))