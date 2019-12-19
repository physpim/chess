class Position:
    # Class for position type,
    def __init__(self, position: list):
        if len(position) != 2:
            raise ValueError("position length is not 2")
        if not (0 <= position[0] <= 7 and 0 <= position[1] <= 7):
            raise ValueError("position is not within the board")
        self.position = position

    def __add__(self, other):
        # Overloading the add (+) operator
        x = self.position[0] + other.position[0]
        y = self.position[1] + other.position[1]
        return Position([x, y])

    def __mul__(self, factor: int):
        x = factor * self.position[0]
        y = factor * self.position[1]
        return Position([x, y])

    def __eq__(self, other) -> bool:
        # Overloading the equals (==) operator
        return self.position[0] == other.position[0] and \
            self.position[1] == other.position[1]
