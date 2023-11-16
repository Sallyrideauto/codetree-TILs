def min_walking_distance(A, B, x, y):
    # A부터 B까지의 거리 계산
    direct_walk = abs(B - A)

    # A부터 텔레포트 시작 지점까지 걸어간 후 텔레포트 도착 지점에서 B까지 걷는 거리
    # x부터 y까지 또는 y부터 x까지
    teleport_walk = abs(A - x) + abs(B - y) # A -> x -> y -> B
    teleport_walk_alt = abs(A - y) + abs(B - x) # A -> y -> x -> B

    # 세 개의 거리 중에서 가장 짧은 거리 찾기
    return min(direct_walk, teleport_walk, teleport_walk_alt)

A, B, x, y = map(int, input().split())
print(min_walking_distance(A, B, x, y))