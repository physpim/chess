from .piece import Piece, Position


class Pawn(Piece):
    # Class of the pawn piece
    init_position = {0: {0: Position([0, 1]),
                         1: Position([1, 1]),
                         2: Position([2, 1]),
                         3: Position([3, 1]),
                         4: Position([4, 1]),
                         5: Position([5, 1]),
                         6: Position([6, 1]),
                         7: Position([7, 1])},
                     1: {0: Position([0, 6]),
                         1: Position([1, 6]),
                         2: Position([2, 6]),
                         3: Position([3, 6]),
                         4: Position([4, 6]),
                         5: Position([5, 6]),
                         6: Position([6, 6]),
                         7: Position([7, 6])}}
    init_moves = {0: {0: [Position([0, 2]), Position([0, 3])],
                      1: [Position([1, 2]), Position([1, 3])],
                      2: [Position([2, 2]), Position([2, 3])],
                      3: [Position([3, 2]), Position([3, 3])],
                      4: [Position([4, 2]), Position([4, 3])],
                      5: [Position([5, 2]), Position([5, 3])],
                      6: [Position([6, 2]), Position([6, 3])],
                      7: [Position([7, 2]), Position([7, 3])]},
                  1: {0: [Position([0, 5]), Position([0, 4])],
                      1: [Position([1, 5]), Position([1, 4])],
                      2: [Position([2, 5]), Position([2, 4])],
                      3: [Position([3, 5]), Position([3, 4])],
                      4: [Position([4, 5]), Position([4, 4])],
                      5: [Position([5, 5]), Position([5, 4])],
                      6: [Position([6, 5]), Position([6, 4])],
                      7: [Position([7, 5]), Position([7, 4])]}}

    def __init__(self, color: int, piece_number: int):
        super().__init__(color,
                         Pawn.init_position[color][piece_number],
                         Pawn.init_moves[color][piece_number],
                         piece_type=5,
                         piece_number=piece_number)
