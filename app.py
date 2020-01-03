"""Docstring

Explanaition 
"""
__version__ = "0.1"
__author__ = "Pim Venderbosch"

from interface import Ui

# Initializing the game
ui = Ui()

# Make a turn
while ui.board.check_mate == False:
    ui.turn()
