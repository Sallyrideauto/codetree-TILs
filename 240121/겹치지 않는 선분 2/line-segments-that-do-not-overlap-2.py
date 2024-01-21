def count_non_overlapping_segments(segments):
    """
    주어진 선분들 중에서 서로 겹치지 않는 선분의 수를 계산하는 함수

    :param segments: 각 선분의 (x1, x2) 좌표가 담긴 리스트
    :return: 겹치지 않는 선분의 수
    """
    points = []
    for x1, x2 in segments:
        points.append((x1, 1))  # 시작점
        points.append((x2, -1))  # 끝점

    points.sort()

    non_overlapping = 0  # 겹치지 않는 선분의 수
    current_segments = 0  # 현재 겹치는 선분의 수

    for point, point_type in points:
        if point_type == 1:  # 시작점인 경우
            if current_segments == 0:
                non_overlapping += 1
            current_segments += 1
        else:  # 끝점인 경우
            current_segments -= 1

    return non_overlapping

# 사용자로부터 입력을 받습니다.
N = int(input())  # 첫 줄에 정수 N 입력
user_segments = []  # 사용자로부터 입력받은 선분들을 저장할 리스트

for _ in range(N):
    x1, x2 = map(int, input().split())
    user_segments.append((x1, x2))  # 각 선분의 x1, x2 좌표를 튜플로 리스트에 추가

# 겹치지 않는 선분의 수를 계산하고 출력합니다.
print(count_non_overlapping_segments(user_segments))