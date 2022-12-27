class Color(tuple):
    def __new__(cls, r: int, g: int, b: int):
        return super().__new__(cls, (r, g, b))

    @property
    def r(self) -> int:
        return self[0]

    @property
    def g(self) -> int:
        return self[1]

    @property
    def b(self) -> int:
        return self[2]
