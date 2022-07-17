from game.shared.point import Point
from constants import *

class HUD_element:
    def __init__(self, position = Point(0, 0), color = BLACK, text = ""):
        self._text = text
        self._position = position
        self._color = color

    def get_position(self):
        return(self._position)

    def set_position(self, point):
        self._position = point

    def get_color(self):
        return(self._color)

    def get_text(self):
        return(self._text)

    def set_text(self, text):
        self._text = text