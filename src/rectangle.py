from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны должны быть больше нуля")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def perimeter(self) -> int | float:
        return (self.side_a + self.side_b) * 2

    @property
    def area(self) -> int | float:
        return self.side_a * self.side_b
