from random import choice
from game.objects.mineral import Mineral
from pyray import RED, GREEN, YELLOW, BLUE, VIOLET, ORANGE

class Gem(Mineral):
    """A shiny, colorful rock deemed valuable by society.
    
    Attributes:
        Methods and Attributes inherited from Mineral (and by extension Object)
        text: The text symbol representing the Gem
        color: The font color of the Gem
        points: The point value of the gem

    """
    def __init__(self):
        """Constructs a new Gem and inherits methods
           and attributes from Mineral
        
        Args:
            self (Gem): An instance of Gem
        """
        super().__init__()
        self._text =choice(["$", "¢", "£", "¤", "¥"])
        self._color = choice([RED, GREEN, YELLOW, BLUE, VIOLET, ORANGE])
        self._points = self._value(self._color)
         
    def _value(self, color):
        """Assigns a point value to the gem based on its color
        
        Args:
            self (Gem): An instance of Gem
            color: The font color of the gem
        """

        if color == RED: points = 50
        elif color == GREEN: points = 100
        elif color == YELLOW: points = 150
        elif color == BLUE: points = 200
        elif color == VIOLET: points = 250
        elif color == ORANGE: points = 300

        return(points)


