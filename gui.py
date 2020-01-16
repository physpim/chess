from game import Position, Board, Piece
import tkinter as tk
from itertools import product
from functools import partial


class Gui():
    """Grafical user interface for playing chess"""
    color_dict = {0: '#FFFFFF', 1: '#b0b0b0'}
    piece_type_dict = {0: {0: '\u2654', 1: '\u265a'},
                       1: {0: '\u2655', 1: '\u265b'},
                       2: {0: '\u2656', 1: '\u265c'},
                       3: {0: '\u2657', 1: '\u265d'},
                       4: {0: '\u2658', 1: '\u265e'},
                       5: {0: '\u2659', 1: '\u265f'}}
    turn_color_dict = {0: 'White', 1: 'Black'}

    def __init__(self):
        # Init board
        self.board = Board()
        # Init root
        self.root = tk.Tk()
        # Create general structure
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self.test_frame = tk.Label(
            self.root, text='Welcome', font='Courier 20')
        self.test_frame.pack()
        # Create buttons/fields
        self.buttons = [[], [], [], [], [], [], [], []]
        self.fields = [[], [], [], [], [], [], [], []]
        for x, y in product(range(8), range(8)):
            field_color = (x + y) % 2
            self.fields[x].append(
                tk.Frame(self.board_frame,
                         height=50,
                         width=50,
                         background=Gui.color_dict[field_color])
            )
            self.fields[x][y].propagate(False)
            self.fields[x][y].grid(column=x, row=y)
            self.buttons[x].append(
                tk.Button(self.fields[x][y],
                          background=Gui.color_dict[field_color],
                          activebackground='#f2ff00',
                          borderwidth=0,
                          font='Courier 30')
            )
            self.buttons[x][y].pack(fill='both', expand=True)
        self.draw()
        self.select_piece()
        self.root.mainloop()

    def select_piece(self):
        """Select piece to move"""
        color = self.board.turn_color
        color_str = Gui.turn_color_dict[color]
        self.test_frame.configure(text=(color_str + ', it\'s your turn'))
        for x, rows in enumerate(self.buttons):
            for y, button in enumerate(rows):
                piece = self.board.find_piece(Position(x, y))
                if piece.color == color and \
                   piece.moves != [] and \
                   piece.moves != None:
                    func = partial(self.show_moves, piece)
                    button.configure(
                        command=func
                    )

    def show_moves(self, piece: Piece):
        """Marks the fields where the selected piece can move to"""
        self.reset_buttons()
        for move in piece.moves:
            self.buttons[move.x][move.y].configure(
                background='#f2ff00',
                command=partial(self.select_move, piece, move)
            )

    def select_move(self, piece, position):
        """Runs when player selects where to move to"""
        self.reset_buttons()
        self.board.recalculate(piece, position)
        self.board.delete_self_check()
        self.board.turn_counter += 1
        self.board.turn_color = int(not self.board.turn_color)
        self.draw()
        if self.board.check == True:
            self.board.check_mate = \
                self.board.ischeckmate(self.board.turn_color)
            if self.board.check_mate == True:
                self.check_mate()
            else:
                self.check()
        self.select_piece()

    def draw(self):
        """Draws pieces on the board"""
        for (x, y) in product(range(8), range(8)):
            piece = self.board.find_piece(Position(x, y))
            if piece.color != None:
                self.buttons[x][y].config(
                    text=Gui.piece_type_dict[piece.type][piece.color]
                )
            else:
                self.buttons[x][y].config(text='')

    def check(self):
        """Runs when game is check"""
        self.test_frame.configure(text='Check!')

    def check_mate(self):
        """Runs when game is check mate"""
        self.test_frame.configure(text='Check mate! The game is over...')

    def reset_buttons(self):
        """Resets the buttons colors and commands"""
        for x, y in product(range(8), range(8)):
            button = self.buttons[x][y]
            button.configure(
                command=False,
                background=Gui.color_dict[(x + y) % 2]
            )


if __name__ == '__main__':
    g = Gui()
