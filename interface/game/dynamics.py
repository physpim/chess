from .piece_types import Position


class Dynamics:
    # Class that manages the game dynamics: performing a turn, check(mate) detection
    def __init__(self):
        # Initializing the game settings
        self.turn_counter = 0
        self.turn_color = 0
        self.check: bool = False
        self.check_mate: bool = False
