import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimeter, area",
    [
        (3, 4, 5, 12, 4.898979485566356),
        (3.5, 4.5, 5.5, 13.5, 6.535659396725016)
    ],
    ids=['integer', 'float']
)
def test_triangle_positive(side_a, side_b, side_c, perimeter, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"
    assert t.area == area, f"Площадь должна быть равна {area}"
