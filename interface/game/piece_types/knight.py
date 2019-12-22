from .piece import Piece, Position


class Knight(Piece):
    # Class of the knight piece
    init_position = {0: {0: Position(1, 0), 1: Position(6, 0)},
                     1: {0: Position(1, 7), 1: Position(6, 7)}}
    init_moves = {0: {0: [Position(0, 2), Position(2, 2)],
                      1: [Position(7, 2), Position(5, 2)]},
                  1: {0: [Position(0, 5), Position(2, 5)],
                      1: [Position(0, 5), Position(2, 5)]}}

    def __init__(self, color: int, piece_number: int):
        super().__init__(color,
                         Knight.init_position[color][piece_number],
                         Knight.init_moves[color][piece_number],
                         piece_type=4,
                         piece_number=piece_number)
