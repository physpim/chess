from .piece import Piece, Position


class Rook(Piece):
    # Class of the rook piece
    init_position = {0: {0: Position([0, 0]), 1: Position([7, 0])},
                     1: {0: Position([0, 7]), 1: Position([7, 7])}}
    init_moves = []

    def __init__(self, color: int, piece_number: int):
        super().__init__(color,
                         Rook.init_position[color][piece_number],
                         Rook.init_moves,
                         piece_type=2,
                         piece_number=piece_number)

    def valid_directions(self):
        # Determines valid moves for rook that are within the bounds of the
        # board. Doesn't account for other pieces being in the way.
        directions = ([1, 0], [0, 1], [-1, 0], [0, -1])
        m = [7] * len(directions)
        return (directions, m)

