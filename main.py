import math


class vec2:
    def __init__(self, x: int | float = 0.0, y: int | float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return self.__repr__()

    def radian_heading(self):
        if self.x:
            return math.atan(self.y/self.x)
        return 0.0

    def deg_heading(self):
        return (self.radian_heading()) * (180/math.pi)

    def mag(self) -> float:
        return float(math.fabs(math.sqrt((self.x**2 + self.y**2))))

    def dist(self, other: "vec2") -> float:
        return float(math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2))

    def limit(self, limit: int | float):
        limit = float(limit)
        if self.x > limit:
            self.x = limit
        if self.y > limit:
            self.y = limit

    def __lt__(self, other: "vec2") -> bool:
        return self.mag() < other.mag()

    def __le__(self, other: "vec2") -> bool:
        return self.mag() <= other.mag()

    def __eq__(self, other: "vec2") -> bool:
        return self.mag() == other.mag()

    def __ne__(self, other: "vec2") -> bool:
        return self.mag() != other.mag()

    def __gt__(self, other: "vec2") -> bool:
        return self.mag() > other.mag()

    def __ge__(self, other: "vec2") -> bool:
        return self.mag() >= other.mag()

    def __add__(self, other: "vec2"):
        return vec2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: "vec2"):
        self.__add__(other)

    def __radd__(self, other: "vec2"):
        self.__add__(other)

    def __sub__(self, other: "vec2"):
        return vec2(self.x - other.x, self.y - other.y)

    def __isub__(self, other: "vec2"):
        self.__sub__(other)

    def __rsub__(self, other: "vec2"):
        self.__sub__(other)

    def __mul__(self, other: "vec2"):
        return vec2(self.x * other.x, self.y * other.y)

    def __imul__(self, other: "vec2"):
        self.__mul__(other)

    def __rmul__(self, other: "vec2"):
        self.__mul__(other)

    def __divmod__(self, other: "vec2"):
        if other.x and other.y:
            return vec2(self.x / other.x, self.y / other.y)
        else:
            raise ValueError()

    def __idivmod__(self, other: "vec2"):
        self.__divmod__(other)

    def __rdivmod__(self, other: "vec2"):
        self.__divmod__(other)

    def __floor__(self) -> "vec2":
        return vec2(math.floor(self.x), math.floor(self.y))

    def __ceil__(self) -> "vec2":
        return vec2(math.ceil(self.x), math.ceil(self.y))
