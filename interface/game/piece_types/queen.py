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

    def valid_directions(self):
        # Determines valid moves for queen that are within the bounds of the
        # board. Doesn't account for other pieces being in the way.
        directions = ([1, 0], [1, 1], [0, 1], [-1, 1],
                      [-1, 0], [-1, -1], [0, -1], [1, -1])
        m = [7] * len(directions)
        return (directions, m)
