from audioop import minmax
from game.shared.point import Point
from game.hud import HUD_element
from random import choice
from constants import *

class Block(HUD_element):
    def __init__(self):
        super().__init__()
        self._position = Point(CELL_SIZE*(COLUMNS+3), CELL_SIZE*11)
        self._rotations = [self.zero_deg, self.ninety_deg, self.one_eighty_deg, self.two_seventy_deg]
        self._rotation = 0
        pass

    def get_squares(self):
        return(self._squares)

    def remove_square(self, square):
        self._squares.remove(square)

    def get_limits(self):
        minY = 1000
        maxY = -1000
        minX = 1000
        maxX = -1000

        for square in self._squares:
            y = square.get_position().get_y()
            if y < minY: minY = y
            if y + CELL_SIZE > maxY: maxY = y + CELL_SIZE

            x = square.get_position().get_x()
            if x < minX: minX = x
            if x + CELL_SIZE > maxX: maxX = x + CELL_SIZE
        return(minY, maxY, minX, maxX)

    def rotate_block(self):
        if self._rotation < 3:
            self._rotation += 1
        else: self._rotation = 0
        
    def get_rotation(self):
        self._rotations[self._rotation]()