import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimeter, area",
    [
        (3, 4, 5, 12, round(4.898979485566356, 2)),
        (3.5, 4.5, 5.5, 13.5, round(6.535659396725016, 2))
    ],
    ids=['integer', 'float']
)
def test_triangle_positive(side_a, side_b, side_c, perimeter, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"
    assert t.area == area, f"Площадь должна быть равна {area}"


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (1, 2, 3),
        (1.5, 2.5, 7.5)
    ],
    ids=['integer', 'float']
)
def test_triangle_with_incorrect_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError) as info:
        Triangle(side_a, side_b, side_c)
    assert 'Треугольника с такими сторонами не существует' in str(info.value)


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (-1, 2, 3),
        (1.5, 2.5, -7.5),
        (0, 2, 3),
        (1.0, 3.2, 0.0)
    ],
    ids=['negative_integer', 'negative_float', 'zero_integer', 'zero_float']
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError) as info:
        Triangle(side_a, side_b, side_c)
    assert 'Стороны треугольника должны быть больше нуля' in str(info.value)
