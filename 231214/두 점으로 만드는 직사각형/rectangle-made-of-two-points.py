def minimum_area(x1, y1, x2, y2, a1, b1, a2, b2):
    # Calculate the minimum and maximum coordinates for the inclusive rectangle
    min_x = min(x1, a1)
    max_x = max(x2, a2)
    min_y = min(y1, b1)
    max_y = max(y2, b2)

    # Calculate the width and height if the inclusive rectangle
    width = max_x - min_x
    height = max_y - min_y

    # Calculate the area of the inclusive rectangle
    area = width * height

    return area

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

print(minimum_area(x1, y1, x2, y2, a1, b1, a2, b2))