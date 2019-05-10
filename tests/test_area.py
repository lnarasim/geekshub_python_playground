import pytest
from geekshub_pyproblems.area import area_of_circle, area_of_rectangle, area_of_square
import math


def test_area_of_circle_valid_values():
    radius = 4
    area = area_of_circle(radius)
    assert area == math.pi * radius * radius

    radius = 10
    area = area_of_circle(radius)
    assert area == math.pi * radius * radius

    radius = 100
    area = area_of_circle(radius)
    assert area == math.pi * radius * radius

    radius = 4.1
    area = area_of_circle(radius)
    assert area == math.pi * radius * radius

    radius = 100.1
    area = area_of_circle(radius)
    assert area == math.pi * radius * radius

    radius = 0
    area = area_of_circle(radius)
    assert area == math.pi * radius * radius


def test_area_of_circle_invalid_values():
    radius = -1
    with pytest.raises(ValueError):
        area = area_of_circle(radius)

    radius = -100
    with pytest.raises(ValueError):
        area = area_of_circle(radius)

    radius = "str"
    with pytest.raises(ValueError):
        area = area_of_circle(radius)

    radius = None
    with pytest.raises(ValueError):
        area = area_of_circle(radius)

    radius = []
    with pytest.raises(ValueError):
        area = area_of_circle(radius)


def test_area_of_rectangle_valid_values():
    length = 10
    breadth = 200
    area = area_of_rectangle(length, breadth)
    assert area == length * breadth

    length = 0
    breadth = 200
    area = area_of_rectangle(length, breadth)
    assert area == length * breadth

    length = 10
    breadth = 0
    area = area_of_rectangle(length, breadth)
    assert area == length * breadth

    length = 100
    breadth = 200
    area = area_of_rectangle(length, breadth)
    assert area == length * breadth

    length = 100.1
    breadth = 200
    area = area_of_rectangle(length, breadth)
    assert area == length * breadth

    length = 100
    breadth = 200.1
    area = area_of_rectangle(length, breadth)
    assert area == length * breadth


def test_area_of_rectangle_invalid_values():
    length = -10
    breadth = 200
    with pytest.raises(ValueError):
        area_of_rectangle(length, breadth)

    length = 10
    breadth = -200
    with pytest.raises(ValueError):
        area_of_rectangle(length, breadth)

    length = -10
    breadth = -200
    with pytest.raises(ValueError):
        area_of_rectangle(length, breadth)

    length = "str"
    breadth = 200
    with pytest.raises(ValueError):
        area_of_rectangle(length, breadth)

    length = None
    breadth = 200
    with pytest.raises(ValueError):
        area_of_rectangle(length, breadth)

    length = 10
    breadth = "float"
    with pytest.raises(ValueError):
        area_of_rectangle(length, breadth)


def test_area_of_square_valid_values():
    side = 10
    area = area_of_square(side)
    assert area == side * side * side

    side = 100
    area = area_of_square(side)
    assert area == side * side

    side = 200.1
    area = area_of_square(side)
    assert area == side * side

    side = 1000.1011
    area = area_of_square(side)
    assert area == side * side


def test_area_of_square_invalid_values():
    side = -10
    with pytest.raises(ValueError):
        area_of_square(side)

    side = "Hello"
    with pytest.raises(ValueError):
        area_of_square(side)


    side = []
    with pytest.raises(ValueError):
        area_of_square(side)


    side = [1, 2]
    with pytest.raises(ValueError):
        area_of_square(side)
