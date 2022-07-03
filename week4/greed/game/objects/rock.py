from random import choice
from game.objects.mineral import Mineral
from pyray import BROWN

class Rock(Mineral):
    """A dirty, brown rock with no value  
    Attributes:
        Methods and Attributes inherited from Mineral (and by extension Object)
        text: The text symbol representing the Gem
        color: The font color of the Gem
        points: The point value of the gem

    """
    def __init__(self):
        """Constructs a new Rock and inherits methods
           and attributes from Mineral
        
        Args:
            self (Rock): An instance of Rock
        """
        super().__init__()
        self._color = BROWN
        self._text = choice(["O", "o", "0", "@"])
        self._points = -100