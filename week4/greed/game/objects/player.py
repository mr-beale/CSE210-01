from pyray import WHITE
from game.objects.object import Object
from game.services.keyboardService import KeyboardService

class Player(Object):
    """The object that is controlled by the user. It is responsible for
       moving around the screen and collecting gems.

    Attributes:
        color (pyray color): The color of the character in the window
        x (int): The x coordinate of where the character is in the window
        y (int): The y coordinate of where the character is in the window
        size (int): The size of the font
        text (String): The text representing the character in the window
        keys (KyeboardService) handles the user input from the keyboard  
    """
    def __init__(self):
        """Constructs a new Player and inherits methods from Object
        
        Args:
            self (Player): an instance of Player
        """
        self._color = WHITE
        self._x = 390
        self._y = 425
        self._size = 20
        self._text = "#"

        self._keys = KeyboardService()

    def move(self):
        """Listens for keyboard input and updates the xy coordinates of the player
           in the window.

        Args:
            self (Player): An instance of Player   
        """
        dx, dy = self._keys.get_direction()
        x = self._x + dx
        y = self._y + dy
        if (x < 780 and x > 10):
            self._x += dx
        if y < 430 and y > 325:
            self._y += dy