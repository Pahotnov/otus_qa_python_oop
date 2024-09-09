import math

from src.figure import Figure


class Triangle(Figure):
    def __init__(self,
                 side_a: int | float,
                 side_b: int | float,
                 side_c: int | float
                 ):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть больше нуля")
        elif (
                (side_a >= (side_b + side_c)) or
                (side_b >= (side_a + side_c)) or
                (side_c >= (side_a + side_b))
        ):
            raise ValueError("Треугольника с такими сторонами не существует")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_perimeter(self) -> int | float:
        return self.side_a + self.side_b + self.side_c

    @property
    def get_area(self) -> int | float:
        half_perimeter = self.get_perimeter / 2
        area = math.sqrt(
            half_perimeter *
            (half_perimeter - self.side_b) *
            (half_perimeter - self.side_b) *
            (half_perimeter - self.side_c)
                         )
        return area
