# 입력 받기
N = int(input())  # 좌석의 개수 N
seat = list(input())   # 좌석 상태를 나타내는 문자열

def min_dist():
    dist = N
    # 둘 다 1인 곳에 대해 모든 쌍을 조사하여, 그 중 가장 가까운 거리 구하기
    for i in range(N):
        for j in range(i + 1, N):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)

    return dist

ans = 0
# 들어갈 위치를 일일이 정해 보며 그 상황에서 가장 가까운 사람간의 거리를 구해 가능한 경우 중 최대값 계산
for i in range(N):
    if seat[i] == '0':
        # 비어있는 위치에 인원 배치
        seat[i] = '1'
        # 가장 가까운 사람 간 거리를 구해 최대값을 갱신
        ans = max(ans, min_dist())
        # 다시 채워 줬던 값을 되돌려 줌
        seat[i] = '0'

print(ans)