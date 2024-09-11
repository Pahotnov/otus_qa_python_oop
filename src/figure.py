from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def perimeter(self) -> int | float:
        pass

    @property
    @abstractmethod
    def area(self) -> int | float:
        pass

    def add_area(self, figure) -> int | float:
        if not isinstance(figure, Figure):
            raise ValueError("Должна быть фигура")
        return self.area + figure.area
