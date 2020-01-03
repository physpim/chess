"""Docstring

Explanaition 
"""
__version__ = "0.1"
__author__ = "Pim Venderbosch"

from interface import Ui

# Initializing the game
ui = Ui()

# Make a turn
for n in range(8):
    ui.turn()
