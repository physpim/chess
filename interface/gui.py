from game import Position, Board, Piece
import tkinter as tk


class Gui():
    """Grafical user interface for playing chess"""

    def __init__(self):
        self.board = Board()
        self.root = tk.Tk()
        self.buttons = [[], [], [], [], [], [], [], []]
        self.fields = [[], [], [], [], [], [], [], []]
        color_dict = {0: '#000000', 1: '#FFFFFF'}
        for x in range(8):
            for y in range(8):
                field_color = (x + y) % 2
                print(field_color)
                self.fields[x].append(
                    tk.Frame(self.root,
                             height=50,
                             width=50,
                             background=color_dict[field_color])
                    )
                self.fields[x][y].propagate(False)
                self.fields[x][y].grid(column=x, row=y)
                self.buttons[x].append(
                    tk.Button(self.fields[x][y],
                    background=color_dict[field_color])
                    )
                self.buttons[x][y].pack()
        # Start application
        self.root.mainloop()


if __name__ == '__main__':
    g = Gui()
