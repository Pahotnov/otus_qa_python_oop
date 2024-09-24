import math

import pytest

from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(
    "radius, perimeter, area",
    [
        (1, 2 * math.pi, math.pi),
        (1.5, 3 * math.pi, math.pi * 2.25)
    ],
    ids=['integer', 'float']
)
def test_circle_positive(radius, perimeter, area):
    c = Circle(radius)
    assert c.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"
    assert c.area == area, f"Площадь должна быть равна {area}"


@pytest.mark.parametrize(
    "radius, side_a, side_b, side_c, area_sum",
    [
        (1, 3, 4, 5, round(8.040572139156149, 2)),
        (1.0, 3.5, 4.5, 5.5, round(9.67725205031481, 2))
    ],
    ids=['integer', 'float']
)
def test_circle_add_triangle_area(radius, side_a, side_b, side_c, area_sum):
    c = Circle(radius)
    t = Triangle(side_a, side_b, side_c)
    assert c.add_area(t) == area_sum


@pytest.mark.parametrize(
    "radius",
    [
        -1,
        -1.5,
        0,
        0.0
    ],
    ids=['negative_integer', 'negative_float', 'zero_integer', 'zero_float']
)
def test_circle_negative(radius):
    with pytest.raises(ValueError) as info:
        Circle(radius)
    assert "Радиус окружности должен быть больше нуля" in str(info.value)
