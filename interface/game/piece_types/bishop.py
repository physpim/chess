from .piece import Piece, Position


class Bishop(Piece):
    # Class of the bishop piece
    init_position = {0: {0: Position([2, 0]), 1: Position([5, 0])},
                     1: {0: Position([2, 7]), 1: Position([5, 7])}}
    init_moves = []

    def __init__(self, color: int, piece_number: int):
        super().__init__(color,
                         Bishop.init_position[color][piece_number],
                         Bishop.init_moves,
                         piece_type=3,
                         piece_number=piece_number)
