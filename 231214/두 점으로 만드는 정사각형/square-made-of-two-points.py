def minimum_square_area(x1, y1, x2, y2, a1, b1, a2, b2):
    # Calculate the minimum and maximum coordinate for the inclusive square
    min_x = min(x1, a1)
    max_x = max(x2, a2)
    min_y = min(y1, b1)
    max_y = max(y2, b2)

    # Calculate the width and height of the inclusive area
    width = max_x - min_x
    height = max_y - min_y

    # The side of the square must be at least as long as the longest side of the inclusive area
    side_length = max(width, height)

    # Calculate the area of the square
    area = side_length ** 2

    return area

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

print(minimum_square_area(x1, y1, x2, y2, a1, b1, a2, b2))