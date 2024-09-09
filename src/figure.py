from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def get_perimeter(self) -> int | float:
        pass

    @property
    @abstractmethod
    def get_area(self) -> int | float:
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Должна быть фигура")
        return self.get_area + figure.get_area
