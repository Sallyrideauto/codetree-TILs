import itertools
import math

def calculate_distance(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

def find_minimum_maximum_distance(points, m):
    min_max_distance = float('inf')

    # 가능한 모든 점 m개의 조합을 구합니다.
    for combination in itertools.combinations(points, m):
        max_distance = 0
        # 조합 내에서 가장 먼 두 점 사이의 거리를 구합니다.
        for point1, point2 in itertools.combinations(combination, 2):
            distance = calculate_distance(point1, point2)
            max_distance = max(max_distance, distance)
        # 가장 먼 거리가 최소가 되도록 갱신합니다.
        min_max_distance = min(min_max_distance, max_distance)

    return min_max_distance

def main():
    n, m = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    result = find_minimum_maximum_distance(points, m)
    print(result)

if __name__ == "__main__":
    main()
