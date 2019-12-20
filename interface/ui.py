from .game import Position, Board


class Ui:
    # Command line user interface. Manages all the interaction with the user.
    color_dict = {0: "White", 1: "Black"}
    piece_type_dict = {0: "\u2654\u265a",
                       1: "\u2655\u265b",
                       2: "\u2656\u265c",
                       3: "\u2657\u265d",
                       4: "\u2658\u265e",
                       5: "\u2659\u265f"}
    x_str2int = {"a": 0, "b": 1, "c": 2, "d": 3,
                 "e": 4, "f": 5, "g": 6, "h": 7}
    y_str2int = {"1": 0, "2": 1, "3": 2, "4": 3,
                 "5": 4, "6": 5, "7": 6, "8": 7}
    x_int2str = {0: "a", 1: "b", 2: "c", 3: "d",
                 4: "e", 5: "f", 6: "g", 7: "h"}
    y_int2str = {0: "1", 1: "2", 2: "3", 3: "4",
                 4: "5", 5: "6", 6: "7", 7: "8"}

    def __init__(self):
        self.board = Board()
        self.draw()

    def draw(self):
        # Draws the board configuration in the terminal
        display = "     a  b  c  d  e  f  g  h      \n" + \
                  "________________________________ \n "
        # Loop over all x and y indices
        for j in range(8):
            display += " " + str(j+1) + "|"
            for i in range(8):
                # Find the piece index for position [i, j]
                position_ij = Position([i, j])
                k = self.board.find_piece(position_ij)
                if k != -1:
                    display += " " + \
                        Ui.piece_type_dict[self.board.pieces[k]
                                               .type][self.board.pieces[k].color] + " "
                else:
                    # Draw an empty cell
                    display += " - "
            # New line for different i value
            display += "|" + str(j+1) + " \n "
        display += "_______________________________ \n" + \
                   "     a  b  c  d  e  f  g  h    \n"
        self.board_string = display
        print(display)

    def turn(self):
        # Select piece
        selected_piece = self.select_piece()
        # Show options and select where to move to
        position = self.select_move(selected_piece)
        # Recalculate board
        self.board.recalculate(selected_piece, position)
        # Update dynamics attributes
        self.board.turn_counter += 1
        self.board.turn_color = int(not self.board.turn_color)
        # Redraw the board
        self.draw()

    def select_piece(self) -> int:
        # Asks the user to select a piece to make a move with
        question = Ui.color_dict[self.board.turn_color] + \
            ", your turn! Please select a piece. \n"
        index = -1
        while index == -1 or self.board.pieces[index].color != self.board.turn_color:
            coordinate = input(question)
            position = self.coordinate2position(coordinate)
            index = self.board.find_piece(position)
            question = "No piece of yours at this field, try again!"
        return index

    def select_move(self, selected_piece: int) -> Position:
        # Asks the user where to move the selected piece
        question = "The selected piece can move to " + \
            self.moves2text(selected_piece) + "\n"
        coordinate = input(question)
        position = self.coordinate2position(coordinate)
        return position

    def moves2text(self, selected_piece: int) -> str:
        # Turns a list of positions into a string with coordinates
        moves = self.board.pieces[selected_piece].moves
        text = ""
        for move in moves:
            text += self.position2coordinate(move) + ", "
        return text

    def coordinate2position(self, coordinate: str) -> Position:
        # Converts user input to a position that can be read by board functions.
        x_position = Ui.x_str2int[coordinate[0]]
        y_position = Ui.y_str2int[coordinate[1]]
        position = Position([x_position, y_position])
        return position

    def position2coordinate(self, position: Position) -> str:
        # Converts user a position to a coordinate that can be displayed in the
        # prompt.
        return Ui.x_int2str[position.position[0]] + Ui.y_int2str[position.position[1]]
