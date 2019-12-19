from .piece_types import Bishop, King, Knight, Pawn, Queen, Rook, Position


class Board:
    # Board class consists of all the chess pieces, also defines the moving
    # rules.

    def __init__(self):
        # Initialize board by creating all pieces in a chess game
        self.pieces = []
        for color in range(2):
            # Initialize for both colors: 1 king, 1 queen, 2 rooks, 2 bishops,
            # 2 knights and 8 pawns. All pieces are stored in a list.
            self.pieces.append(King(color))
            self.pieces.append(Queen(color))
            for piece_number in range(2):
                self.pieces.append(Rook(color, piece_number))
            for piece_number in range(2):
                self.pieces.append(Bishop(color, piece_number))
            for piece_number in range(2):
                self.pieces.append(Knight(color, piece_number))
            for piece_number in range(8):
                self.pieces.append(Pawn(color, piece_number))

    def find_piece(self, position: Position) -> int:
        # Returns the index (k) in the array of pieces for a specified position,
        # returns -1 for an empty field
        index = -1
        for i, piece in enumerate(self.pieces):
            if piece.position == position and \
                    piece.alive == True:
                index = i
                break
        return index

    def recalculate(self, selected_piece: int, position: Position):
        # Moves selected_piece to position and recalculates the board 
        self.pieces[selected_piece].position = position
        for piece in self.pieces:
            for i in range(8):
                for j in range(8):
                    # piece.can_move(Position([i,j]))
                    pass
