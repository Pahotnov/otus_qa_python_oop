import math

import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(
    "side_a, side_b, perimeter, area",
    [
        (1, 2, 6, 2),
        (1.5, 2.5, 8.0, 3.75)
    ],
    ids=['integer', 'float']
)
def test_rectangle_positive(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"
    assert r.area == area, f"Площадь должна быть равна {area}"


@pytest.mark.parametrize(
    "side_a, side_b, area_sum",
    [
        (1, 2, 3),
        (1.5, 2.5, 6.0)
    ],
    ids=['integer', 'float']
)
def test_rectangle_add_square_area(side_a, side_b, area_sum):
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    assert r.add_area(s) == area_sum


@pytest.mark.parametrize(
    "side_a, side_b, radius, area_sum",
    [
        (1, 2, 1, math.pi + 2),
        (1.5, 2.5, 1.0, math.pi + 3.75)
    ],
    ids=['integer', 'float']
)
def test_rectangle_add_circle_area(side_a, side_b, radius, area_sum):
    r = Rectangle(side_a, side_b)
    c = Circle(radius)
    assert r.add_area(c) == area_sum


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area_sum",
    [
        (3, 4, 5, 16.898979485566358),
        (3.5, 4.5, 5.5, 22.285659396725016)
    ],
    ids=['integer', 'float']
)
def test_rectangle_add_triangle_area(side_a, side_b, side_c, area_sum):
    r = Rectangle(side_a, side_b)
    t = Triangle(side_a, side_b, side_c)
    assert r.add_area(t) == area_sum
