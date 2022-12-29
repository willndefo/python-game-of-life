class Color(tuple):
    def __new__(cls, r: int = 0, g: int = 0, b: int = 0):
        return super().__new__(cls, (r, g, b))

    def __str__(self):
        return f"{self.r}, {self.g}, {self.b}"

    @property
    def r(self) -> int:
        return self[0]

    @property
    def g(self) -> int:
        return self[1]

    @property
    def b(self) -> int:
        return self[2]


class Size(tuple):
    def __new__(cls, w: int = 0, h: int = 0):
        return super().__new__(cls, (w, h))

    def __str__(self):
        return f"{self.w}, {self.h}"

    @property
    def w(self) -> int:
        return self[0]

    @property
    def h(self) -> int:
        return self[1]
