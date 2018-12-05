from math import pi


class Circle:
    radius: float
    diameter: float

    def __init__(self, r: float = 1.0):
        if r < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = r
        self.diameter = r * 2
        self.area = pi * self.radius * self.radius

    def __eq__(self, other) -> bool:
        return self.radius is other.radius

    def __str__(self) -> str:
        return 'Circle(' + str(self.radius) + ')'

    def __repr__(self) -> str:
        return 'Circle(' + str(self.radius) + ')'
