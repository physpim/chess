from .piece_types import Bishop, King, Knight, Pawn, Queen, Rook, Position, Piece
from copy import deepcopy
from functools import partial


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
        self.history = []

    def turn(self, selected_piece, position, draw, check, check_mate):
        """Performs a turn and executes all interface functions"""
        self.recalculate(selected_piece, position, lambda: 1)
        self.delete_self_check()
        self.turn_counter += 1
        self.turn_color = int(not self.turn_color)
        draw()
        if self.check == True:
            self.check_mate = self.ischeckmate(self.turn_color)
            if self.check_mate == True:
                check_mate()
            else:
                check()

    def find_piece(self, position: Position) -> Piece:
        """Finds piece on position and returns the piece

        nb: When no piece is found at position, a piece with all attributes set to None is returned.
        """
        for piece in self.pieces:
            if piece.position == position and piece.alive == True:
                return piece
        else:
            return Piece(None, None, None, None, None)

    def recalculate(self,
                    selected_piece: Piece,
                    position: Position,
                    ask_promotion_type):
        """Recalculates board when selected_piece moves to Position"""
        type_funcs = {0: self.king, 1: self.queen, 2: self.rook,
                      3: self.bishop, 4: self.knight, 5: self.pawn}
        # Move the selected piece and capture if needed
        self.move(selected_piece, position,
                  lambda: ask_promotion_type())
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
                    copy_board.recalculate(copy_piece, field, lambda: 1)
                    if copy_board.ischeck(copy_piece.color):
                        remove_fields.append(field)
                for elem in remove_fields:
                    piece.moves.remove(elem)

    def move(self,
             selected_piece: Piece,
             position: Position,
             ask_promotion_type):
        """Moves selected_piece to position and captures if needed"""
        self.history.append({'piece': selected_piece,
                             'from': selected_piece.position,
                             'to': position})

        # Normal moving and capturing
        captured_piece = self.find_piece(position)
        if captured_piece.color != None:
            captured_piece.alive = False
            captured_piece.moves = []
        selected_piece.position = position

        # Check for en passant
        if selected_piece.type == 5:
            for captured_piece in selected_piece.en_passant:
                if abs(captured_piece.position - position) == 1:
                    captured_piece.alive = False
                    captured_piece.moves = []
            selected_piece.en_passant = []

        # Check for pawn promotion
        promotion_rows = {0: 7, 1: 0}
        if selected_piece.type == 5 and \
           selected_piece.position.y == promotion_rows[selected_piece.color]:
            self.promote(selected_piece, ask_promotion_type)

    def promote(self, piece: Piece, ask_promotion_type):
        """Regulates promotion of a pawn"""
        promotion_type = ask_promotion_type()
        piece.type = promotion_type
        piece.piece_number = None

    def king(self, piece: Piece):
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

    def queen(self, piece: Piece):
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

    def rook(self, piece: Piece):
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

    def bishop(self, piece: Piece):
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

    def knight(self, piece: Piece):
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

    def pawn(self, piece: Piece):
        """Updates the pawn's piece.moves"""
        # Forward move(s)
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

        # Diagonal (capturing) moves
        capture_directions = {0: [Position(1, 1), Position(-1, 1)],
                              1: [Position(1, -1), Position(-1, -1)]}
        for direction in capture_directions[piece.color]:
            field = piece.position + direction
            if field.within_board() == True:
                piece_on_field = self.find_piece(field)
                if piece_on_field.color != None and \
                   piece_on_field.color != piece.color:
                    piece.moves.append(field)

        # En passant moves
        row_ep = {0: 4, 1: 3}
        if current_position.y == row_ep[piece.color]:
            neighbours = [current_position + Position(1, 0),
                          current_position + Position(-1, 0)]
            piece.en_passant = []
            for position in neighbours:
                piece_on_field = self.find_piece(position)
                if piece_on_field.color != None:
                    if self.history[-1]['piece'] == piece_on_field:
                        distance = abs(self.history[-1]['from'] -
                                       self.history[-1]['to'])
                        if distance == 2:
                            piece.moves.append(
                                position + directions[piece.color]
                            )
                            piece.en_passant.append(piece_on_field)

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
