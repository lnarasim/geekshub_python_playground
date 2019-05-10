"""This module calculates the area of circle, rectangle and square when the
dimensions of their sides/radius.
"""
import math


def is_int_float(value):
    """Checks whether or not the value is a number"""
    return isinstance(value, (int, float)) or False


def area_of_circle(radius):
    """This function calculates area of a circle"""
    if not is_int_float(radius):
        raise ValueError("Invalid type. Pass integral values")
    if radius < 0:
        raise ValueError("Invalid input. Pass positive value")

    return math.pi * radius * radius


def area_of_rectangle(length, breadth):
    """This function calculates area of a rectangle"""
    if not is_int_float(length) or not is_int_float(breadth):
        raise ValueError("Invalid Input")
    if length < 0 or breadth < 0:
        raise ValueError("Invalid input")

    return length * breadth


def area_of_square(side):
    """This function calculates area of a square"""
    return area_of_rectangle(side, side)


