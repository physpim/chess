from .piece_types import Bishop, King, Knight, Pawn, Queen, Rook, Position, Piece


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
        self.turn_counter = 0
        self.turn_color = 0
        self.check: bool = False
        self.check_mate: bool = False

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
        # Move selected_piece to position
        self.pieces[selected_piece].position = position
        # Recalculate the moves for all pieces
        for piece_number, _ in enumerate(self.pieces):
            self.piece_moves(piece_number)

    # Methods that calculate where piece type can move
    def piece_moves(self, piece_number: int):
        # Ensures the right method is called for the specific piece type
        type_dict = {0: self.king, 1: self.queen, 2: self.rook,
                     3: self.bishop, 4: self.knight, 5: self.pawn}
        func = type_dict[self.pieces[piece_number].type]
        return func(piece_number)

    def king(self, piece_number: int) -> list:
        directions = [Position([0, 1]), Position([1, 0]), Position([0, -1]), Position([-1, 0]),
                      Position([1, 1]), Position([1, -1]), Position([-1, 1]), Position([-1, 1])]
        self.pieces[piece_number].moves = []
        for direction in directions:
            field = self.pieces[piece_number].position + direction
            if field.within_board() == True:
                piece_on_field = self.find_piece(field)
                if piece_on_field == -1 or \
                        self.pieces[piece_on_field].color != self.pieces[piece_number].color:
                    self.pieces[piece_number].moves.append(field)
        print(self.pieces[piece_number].moves)

    def queen(self, piece_number: int) -> list:
        pass

    def rook(self, piece_number: int) -> list:
        pass

    def bishop(self, piece_number: int) -> list:
        pass

    def knight(self, piece_number: int) -> list:
        pass

    def pawn(self, piece_number: int) -> list:
        pass
