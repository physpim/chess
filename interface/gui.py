from game import Position, Board, Piece
import tkinter as tk
from itertools import product
from functools import partial


class Gui():
    """Grafical user interface for playing chess"""
    color_dict = {0: '#FFFFFF', 1: '#b0b0b0'}
    piece_type_dict = {0: {1: '\u2654', 0: '\u265a'},
                       1: {1: '\u2655', 0: '\u265b'},
                       2: {1: '\u2656', 0: '\u265c'},
                       3: {1: '\u2657', 0: '\u265d'},
                       4: {1: '\u2658', 0: '\u265e'},
                       5: {1: '\u2659', 0: '\u265f'}}

    def __init__(self):
        # Init board
        self.board = Board()
        # Init root
        self.root = tk.Tk()
        # Create buttons/fields
        self.buttons = [[], [], [], [], [], [], [], []]
        self.fields = [[], [], [], [], [], [], [], []]
        for x, y in product(range(8), range(8)):
            field_color = (x + y) % 2
            self.fields[x].append(
                tk.Frame(self.root,
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
        self.turn()
        self.root.mainloop()

    def turn(self):
        """Performs all actions within a turn"""
        # self.board.turn(self.select_piece,
        #                 self.select_move,
        #                 self.draw,
        #                 self.check,
        #                 self.check_mate)
        self.select_piece()

    def select_piece(self):
        """Select piece to move"""
        color = self.board.turn_color
        for x, rows in enumerate(self.buttons):
            for y, button in enumerate(rows):
                piece = self.board.find_piece(Position(x, y))
                if piece.color != color and \
                   piece.moves != [] and \
                   piece.moves != None:
                    print(piece.position)
                    print(piece.moves)
                    func = partial(self.show_moves, piece.moves)
                    button.configure(
                        command=func
                    )

    def show_moves(self, moves: list):
        """Marks the fields where the selected piece can move to"""
        self.reset_buttons()
        for move in moves:
            self.buttons[move.x][move.y].configure(
                background='#f2ff00',
                command=partial(print, 'this is a movable field')
            )

    def select_move(self):
        pass

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
        pass

    def check_mate(self):
        pass

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
