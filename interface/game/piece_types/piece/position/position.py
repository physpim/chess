class Position:
    # Class for position type,
    def __init__(self, position: list):
        if len(position) != 2:
            raise ValueError("position length is not 2")
        self.position = position

    def __add__(self, other):
        # Overloading the add (+) operator
        x = self.position[0] + other.position[0]
        y = self.position[1] + other.position[1]
        return Position([x, y])

    def __rmul__(self, factor: int):
        x = factor * self.position[0]
        y = factor * self.position[1]
        return Position([x, y])

    def __eq__(self, other) -> bool:
        # Overloading the equals (==) operator
        return self.position[0] == other.position[0] and \
            self.position[1] == other.position[1]

    def __str__(self) -> str:
        return 'Position([' + str(self.position[0]) + ',' + str(self.position[1]) + '])'
    
    def __repr__(self):
        return str(self)

    def within_board(self) -> bool:
        if 0 <= self.position[0] <= 7 and 0 <= self.position[1] <= 7:
            return True
        else:
            return False
