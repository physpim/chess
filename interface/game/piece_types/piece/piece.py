from .position import Position


class Piece:
    # Describes a general chess piece
    __color_dict__ = {0: "white", 1: "black"}
    __piece_type_dict__ = {0: "king", 1: "queen", 2: "rook",
                           3: "bishop", 4: "knight", 5: "pawn"}

    def __init__(self, color: int, position: Position, moves: list, piece_type: int, piece_number: int):
        self.color = color
        self.position = position
        self.moves = moves
        self.type = piece_type
        self.piece_number = piece_number
        self.alive = True
