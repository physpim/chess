from .piece_types import Position
from .board import Board


class Dynamics:
    # Class that manages the game dynamics: performing a turn, check(mate) detection
    def __init__(self):
        # Initializing the game settings
        self.turn_counter = 0
        self.turn_color = 0
        self.check: bool = False
        self.check_mate: bool = False

    def ask_piece_to_move(self, board: Board, coordinate: str, color: int) -> int:
        piece_position = board.coordinate2position(coordinate)
        piece_index = board.find_piece(piece_position)
        while piece_index == -1 or\
                piece_position == Position([-1, -1]) or\
                color != board.pieces[piece_index].color:
            coordinate = list(input("There is no piece of yours on the " +
                                    "selected field, try again.\n"))
            piece_position = board.coordinate2position(coordinate)
            piece_index = board.find_piece(piece_position)
        return piece_index

    def ask_move(self, board: Board, valid_moves: list) -> Position:
        # Show which fields the selected piece can move to
        message = "The selected piece can move to "
        for fields in valid_moves:
            message += board.position2coordinate(fields) + ", "
        message = message[:-2] + ". Which of these do you want to move it " + \
            "to? \n"
        coordinate = input(message)
        new_position = board.coordinate2position(coordinate)
        while new_position not in valid_moves:
            coordinate = input("The selected piece cannot move to this field"
                               ", try again.\n")
            new_position = board.coordinate2position(coordinate)
        return new_position
