import math

import pytest

from src.circle import Circle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(
    "side_a, perimeter, area",
    [
        (1, 4, 1),
        (1.5, 6.0, 2.25)
    ],
    ids=['integer', 'float']
)
def test_square_positive(side_a, perimeter, area):
    s = Square(side_a)
    assert s.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"
    assert s.area == area, f"Площадь должна быть равна {area}"


@pytest.mark.parametrize(
    "side_a, radius, area_sum",
    [
        (1, 1, math.pi + 1),
        (1.5, 1.0, math.pi + 2.25)
    ],
    ids=['integer', 'float']
)
def test_square_add_circle_area(side_a, radius, area_sum):
    s = Square(side_a)
    c = Circle(radius)
    assert s.add_area(c) == area_sum


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area_sum",
    [
        (3, 4, 5, 13.898979485566356),
        (3.5, 4.5, 5.5, 18.785659396725016)
    ],
    ids=['integer', 'float']
)
def test_square_add_triangle_area(side_a, side_b, side_c, area_sum):
    s = Square(side_a)
    t = Triangle(side_a, side_b, side_c)
    assert s.add_area(t) == area_sum
