class Position:
    # Class for position type,
    def __init__(self, x: int, y: int):
        if type(x) is not int or type(y) is not int:
            raise TypeError("x and y should be integers")
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the add (+) operator
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    def __sub__(self, other):
    # Overloading the add (+) operator
        x = self.x - other.x
        y = self.y - other.y
        return Position(x, y)

    def __rmul__(self, factor: int):
        x = factor * self.x
        y = factor * self.y
        return Position(x, y)

    def __eq__(self, other) -> bool:
        # Overloading the equals (==) operator
        return [self.x, self.y] == [other.x, other.y]

    def __abs__(self) -> float:
        x = self.x
        y = self.y
        return (x ** 2 + y ** 2) ** 0.5

    def __str__(self) -> str:
        return 'Position(' + str(self.x) + ',' + str(self.y) + ')'

    def __repr__(self):
        return str(self)
    
    def __floordiv__(self, other):
        return Position(self.x // other, self.y // other)

    def within_board(self) -> bool:
        if 0 <= self.x <= 7 and 0 <= self.y <= 7:
            return True
        else:
            return False
