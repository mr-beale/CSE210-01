from game.shared.point import Point

from game.elements.cycles import Cycle
from game.elements.lives import Lives
import constants
from game.elements.element import Element

class Player(Element):
    """
    The player and all data needed to create one. Represents one of two users in the game

    Attributes:
    lives (Lives): the lives remaining
    cycle (Cycle): The colorful line representing the players movement
    Text (string): the player's name shown on the screen
    """
    def __init__(self):
        """
        Creates a new instance of Player
        """
        super().__init__()
        self.lives = Lives()
        self.cycle = Cycle()
        self._text = ""