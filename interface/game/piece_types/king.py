from .piece import Piece, Position


class King(Piece):
    # Class of the king piece
    init_position = {0: Position(4, 0), 1: Position(4, 7)}
    init_moves = []

    def __init__(self, color: int):
        super().__init__(color,
                         King.init_position[color],
                         King.init_moves,
                         piece_type=0,
                         piece_number=0)
