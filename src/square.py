from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: int | float):
        if side_a <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        super().__init__(side_a, side_a)
        self.side_a = side_a
