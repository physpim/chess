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
                    print("hello")
                    pass

#############################################################

    def valid_moves(self, piece_index: int) -> list:
        # Function returns the available fields for the piece with piece_index
        (directions, multiplier) = self.pieces[piece_index].valid_directions()
        current_position = self.pieces[piece_index].position
        positions = []
        directions_pawn = (([1, 1], [-1, 1]), ([1, -1], [-1, -1]))
        if self.pieces[piece_index].type == 5:
            for direction_pawn in directions_pawn:
                position_ij = current_position + \
                    Position(direction_pawn[self.pieces[piece_index].color])
                k = self.find_piece(position_ij)
                if k != -1 and self.pieces[k].color != self.pieces[piece_index].color:
                    positions.append(position_ij)
        for i, direction in enumerate(directions):
            for j in range(1, multiplier[i]+1):
                position_ij = current_position + Position(direction) * j
                if self.is_within_board(position_ij):
                    k = self.find_piece(position_ij)
                    if k == -1:
                        positions.append(position_ij)
                    elif self.pieces[k].color != self.pieces[piece_index].color and \
                            self.pieces[piece_index].type != 5:
                        positions.append(position_ij)
                        break
                    else:
                        break
                else:
                    break
        return positions

    def is_within_board(self, position: Position) -> bool:
        if 0 <= position.position[0] <= 7 and \
           0 <= position.position[1] <= 7:
            return True
        else:
            return False

    def is_valid_move(self, piece_index: int, position: Position) -> bool:
        # Function returns if the new position for the piece piece_number is
        # allowed.
        return position in self.valid_moves(piece_index)
