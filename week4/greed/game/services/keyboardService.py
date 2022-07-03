from pyray import *

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._get_scale()

    def _get_scale(self):
        """Changes the default cell size to manipulate the speed
        at wich the character moves in the window.
        """
        if is_key_up(KEY_LEFT_SHIFT):
            self._cell_size = 2

        if is_key_down(KEY_LEFT_SHIFT):
            self._cell_size = 5

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        self._get_scale()
        dx = 0
        dy = 0

        if is_key_down(KEY_LEFT):
            dx = -1
        
        if is_key_down(KEY_RIGHT):
            dx = 1
        
        if is_key_down(KEY_UP):
            dy = -1
        
        if is_key_down(KEY_DOWN):
            dy = 1
        
        return (dx*self._cell_size, dy*self._cell_size)