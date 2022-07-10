from game.elements.element import Element
from game.shared.point import Point
import constants

class Wall(Element):
    """
        The Boundaries of the playing arena. Its responsibility is to provide
        a graphical reference for the  size of the arena and constrian players within.
    """
    def __init__(self, width, height, origin, color):
        """
            Creates a new instance of Wall
        """
        super().__init__()
        self._color = color
        self._width = width
        self._height = height
        self._position = origin
