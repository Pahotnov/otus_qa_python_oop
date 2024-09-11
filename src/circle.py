import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError("Радиус окружности должен быть больше нуля")
        self.radius = radius

    @property
    def perimeter(self) -> int | float:
        return self.radius * 2 * math.pi

    @property
    def area(self) -> int | float:
        return math.pi * self.radius ** 2
