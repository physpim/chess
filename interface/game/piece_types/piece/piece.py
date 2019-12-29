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

    def __eq__(self, other):
        color_bool = self.color == other.color
        position_bool = self.position == other.position
        type_bool = self.type == other.type
        piece_number_bool = self.piece_number == other.piece_number
        return color_bool and position_bool and type_bool and piece_number_bool