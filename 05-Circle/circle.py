from math import pi


class Circle:
    """Circle with radius, diameter and area."""
    radius: float
    diameter: float
    area: float

    def __init__(self, r: float = 1.0):
        if r < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return pi * self.radius ** 2

    def __eq__(self, other) -> bool:
        return self.radius is other.radius

    def __str__(self) -> str:
        return f'Circle({self.radius})'

    def __repr__(self) -> str:
        return f'Circle({self.radius})'
