import math


def is_int_float(value):
    return True if isinstance(value, int) or isinstance(value, float) else False


def area_of_circle(radius):
    if not is_int_float(radius):
        raise ValueError("Invalid type. Pass integral values")
    if radius < 0:
        raise ValueError("Invalid input. Pass positive value")

    return math.pi * radius * radius


def area_of_rectangle(length, breadth):
    if not is_int_float(length) or not is_int_float(breadth):
        raise ValueError("Invalid Input")
    if length < 0 or breadth < 0:
        raise ValueError("Invalid input")

    return length * breadth


def area_of_square(side):
    return area_of_rectangle(side, side)