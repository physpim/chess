from game import Position, Board, Piece
import tkinter as tk
from itertools import product


class Gui():
    """Grafical user interface for playing chess"""
    color_dict = {0: '#000000', 1: '#FFFFFF'}
    piece_type_dict = {0: {0: '\u2654', 1: '\u265a'},
                       1: {0: '\u2655', 1: '\u265b'},
                       2: {0: '\u2656', 1: '\u265c'},
                       3: {0: '\u2657', 1: '\u265d'},
                       4: {0: '\u2658', 1: '\u265e'},
                       5: {0: '\u2659', 1: '\u265f'}}


    def __init__(self):
        # Init board
        self.board=Board()
        # Init gui parts
        self.root=tk.Tk()
        self.buttons=[[], [], [], [], [], [], [], []]
        self.fields=[[], [], [], [], [], [], [], []]
        for x, y in product(range(8), range(8)):
            field_color=(x + y) % 2
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
                          text='\u2654',
                          background=Gui.color_dict[field_color],
                          activebackground='#f2ff00',
                          borderwidth=0,
                          foreground=Gui.color_dict[int(not field_color)])
            )
            self.buttons[x][y].pack(fill='both', expand=True)
        # Start application
        self.root.mainloop()


if __name__ == '__main__':
    g=Gui()
