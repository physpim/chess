from .piece import Piece, Position


class Queen(Piece):
    # Class of the queen piece
    init_position = {0:  Position([3, 0]), 1:  Position([3, 7])}
    init_moves = []

    def __init__(self, color: int):
        super().__init__(color,
                         Queen.init_position[color],
                         Queen.init_moves,
                         piece_type=1, piece_number=0)
