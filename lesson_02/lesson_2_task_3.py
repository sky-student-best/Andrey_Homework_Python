import math


def square(side):

    area = side * side
    return math.ceil(area)


side_value = 3.4
result = square(side_value)
print(f"Сторона: {side_value}, площадь (округлённая вверх): {result}")
