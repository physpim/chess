from .piece import Piece, Position


class King(Piece):
    # Class of the king piece
    init_position = {0: Position([4, 0]), 1: Position([4, 7])}
    init_moves = []

    def __init__(self, color: int):
        super().__init__(color,
                         King.init_position[color],
                         King.init_moves,
                         piece_type=0,
                         piece_number=0)

    def valid_directions(self):
        # Determines valid moves for king that are within the bounds of the
        # board. Doesn't account for other pieces being in the way.
        directions = ([1, 0], [1, 1], [0, 1], [-1, 1],
                      [-1, 0], [-1, -1], [0, -1], [1, -1])
        m = [1] * len(directions)
        return (directions, m)
