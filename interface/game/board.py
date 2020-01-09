from .piece_types import Bishop, King, Knight, Pawn, Queen, Rook, Position, Piece
from copy import deepcopy


class Board:
    """Class that defines the board and incorporates all rules"""
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

    def turn(self, select_piece, select_move, draw, check, check_mate):
        """Performs a turn and executes all interface functions"""
        selected_piece = select_piece()
        position = select_move(selected_piece)
        self.recalculate(selected_piece, position)
        self.delete_self_check()
        self.turn_counter += 1
        self.turn_color = int(not self.turn_color)
        draw()
        if self.check == True:
            self.check_mate = self.ischeckmate(self.turn_color)
            if self.check_mate == True:
                check_mate()
            else: check()


    def find_piece(self, position: Position) -> Piece:
        """Finds piece on position and returns the piece

        nb: When no piece is found at position, a piece with all attributes set to None is returned.
        """
        for piece in self.pieces:
            if piece.position == position and piece.alive == True:
                return piece
        else:
            return Piece(None, None, None, None, None)

    def recalculate(self, selected_piece: Piece, position: Position):
        """Recalculates board when selected_piece moves to Position"""
        type_funcs = {0: self.king, 1: self.queen, 2: self.rook,
                      3: self.bishop, 4: self.knight, 5: self.pawn}
        # Move the selected piece and capture if needed
        self.move(selected_piece, position)
        # Recalculate the moves for all pieces
        for piece in self.pieces:
            piece.moves = []
            func = type_funcs[piece.type]
            func(piece)
        # Detect check
        self.check = self.ischeck(int(not self.turn_color))

    def delete_self_check(self):
        """Delete moves that cause self check"""
        for piece in self.pieces:
            if piece.color != self.turn_color:
                remove_fields = []
                for field in piece.moves:
                    copy_board = deepcopy(self)
                    index = copy_board.pieces.index(piece)
                    copy_piece = copy_board.pieces[index]
                    copy_board.recalculate(copy_piece, field)
                    if copy_board.ischeck(copy_piece.color):
                        remove_fields.append(field)
                for elem in remove_fields:
                    piece.moves.remove(elem)

    def move(self, selected_piece: Piece, position: Position):
        """Moves selected_piece to position and captures if needed"""
        captured_piece = self.find_piece(position)
        if captured_piece.color != None:
            captured_piece.alive = False
            captured_piece.moves = []
        selected_piece.position = position

    def king(self, piece: Piece) -> list:
        """Updates the king's piece.moves"""
        directions = [Position(0, 1), Position(1, 0),
                      Position(0, -1), Position(-1, 0),
                      Position(1, 1), Position(-1, -1),
                      Position(1, -1), Position(-1, 1)]
        for direction in directions:
            field = piece.position + direction
            if field.within_board() == True:
                piece_on_field = self.find_piece(field)
                if piece_on_field.color == None or \
                   piece_on_field.color != piece.color:
                    piece.moves.append(field)

    def queen(self, piece: Piece) -> list:
        """Updates the queen's piece.moves"""
        directions = [Position(0, 1), Position(1, 0),
                      Position(0, -1), Position(-1, 0),
                      Position(1, 1), Position(-1, -1),
                      Position(1, -1), Position(-1, 1)]
        for direction in directions:
            for n in range(1, 8):
                field = piece.position + n * direction
                if field.within_board() == True:
                    piece_on_field = self.find_piece(field)
                    if piece_on_field.color == None:
                        piece.moves.append(field)
                    elif piece_on_field.color != piece.color:
                        piece.moves.append(field)
                        break
                    else:
                        break

    def rook(self, piece: Piece) -> list:
        """Updates the rooks's piece.moves"""
        directions = [Position(0, 1), Position(1, 0),
                      Position(0, -1), Position(-1, 0)]
        for direction in directions:
            for n in range(1, 8):
                field = piece.position + n * direction
                if field.within_board() == True:
                    piece_on_field = self.find_piece(field)
                    if piece_on_field.color == None:
                        piece.moves.append(field)
                    elif piece_on_field.color != piece.color:
                        piece.moves.append(field)
                        break
                    else:
                        break

    def bishop(self, piece: Piece) -> list:
        """Updates the bishop's piece.moves"""
        directions = [Position(1, 1), Position(-1, -1),
                      Position(1, -1), Position(-1, 1)]
        for direction in directions:
            for n in range(1, 8):
                field = piece.position + n * direction
                if field.within_board() == True:
                    piece_on_field = self.find_piece(field)
                    if piece_on_field.color == None:
                        piece.moves.append(field)
                    elif piece_on_field.color != piece.color:
                        piece.moves.append(field)
                        break
                    else:
                        break

    def knight(self, piece: Piece) -> list:
        """Updates the knight's piece.moves"""
        directions = [Position(1, 2), Position(2, 1),
                      Position(1, -2), Position(-2, 1),
                      Position(-1, 2), Position(2, -1),
                      Position(-1, -2), Position(-2, -1)]
        for direction in directions:
            field = piece.position + direction
            if field.within_board() == True:
                piece_on_field = self.find_piece(field)
                if piece_on_field.color == None or \
                        piece_on_field.color != piece.color:
                    piece.moves.append(field)

    def pawn(self, piece: Piece) -> list:
        """Updates the pawn's piece.moves"""
        directions = {0: Position(0, 1), 1: Position(0, -1)}
        current_position = piece.position
        initial_position = Pawn.init_position[piece.color][piece.piece_number]
        if current_position == initial_position:
            n_moves = 2
        else:
            n_moves = 1
        for n in range(1, n_moves+1):
            field = piece.position + n * directions[piece.color]
            if field.within_board() == True:
                piece_on_field = self.find_piece(field)
                if piece_on_field.color == None:
                    piece.moves.append(field)
                else:
                    break
        capture_directions = {0: [Position(1, 1), Position(-1, 1)],
                              1: [Position(1, -1), Position(-1, -1)]}
        for direction in capture_directions[piece.color]:
            field = piece.position + direction
            if field.within_board() == True:
                piece_on_field = self.find_piece(field)
                if piece_on_field.color != None and piece_on_field.color != piece.color:
                    piece.moves.append(field)

    def ischeck(self, color: int) -> bool:
        """Returns if color is check"""
        # Find the king of the right color
        for piece in self.pieces:
            if piece.type == 0 and piece.color == color:
                break
        king_position = piece.position
        # See if other pieces attack the king
        for piece in self.pieces:
            if piece.color != color and \
               king_position in piece.moves and \
               piece.alive == True:
                return True
        else:
            return False

    def ischeckmate(self, color: int) -> bool:
        """Returns if color is check mate"""
        for piece in self.pieces:
            if piece.color == color and piece.moves != []:
                return False
        else:
            return True
