from game.blocks.block import Block
from game.shared.point import Point
from game.hud import HUD_element
from constants import *

class T_block(Block):
    def __init__(self):
        super().__init__()
        self._color = VIOLET
        self.zero_deg()

    def zero_deg(self):
        position = self.get_position()
        self._first = HUD_element(position)
        self._second = HUD_element(position.add(Point(0, -CELL_SIZE)))
        self._third = HUD_element(position.add(Point(-CELL_SIZE, 0)))
        self._fourth = HUD_element(position.add(Point(CELL_SIZE, 0)))

        self._squares = [self._first, self._second, self._third, self._fourth]

    def ninety_deg(self):
        position = self.get_position()
        self._first = HUD_element(position)
        self._second = HUD_element(position.add(Point(-CELL_SIZE, 0)))
        self._third = HUD_element(position.add(Point(0, CELL_SIZE)))
        self._fourth = HUD_element(position.add(Point(0, -CELL_SIZE)))

        self._squares = [self._first, self._second, self._third, self._fourth]

    def one_eighty_deg(self):
        position = self.get_position()
        self._first = HUD_element(position)
        self._second = HUD_element(position.add(Point(0, CELL_SIZE)))
        self._third = HUD_element(position.add(Point(CELL_SIZE, 0)))
        self._fourth = HUD_element(position.add(Point(-CELL_SIZE, 0)))

        self._squares = [self._first, self._second, self._third, self._fourth]

    def two_seventy_deg(self):
        position = self.get_position()
        self._first = HUD_element(position)
        self._second = HUD_element(position.add(Point(CELL_SIZE, 0)))
        self._third = HUD_element(position.add(Point(0, -CELL_SIZE)))
        self._fourth = HUD_element(position.add(Point(0, CELL_SIZE)))

        self._squares = [self._first, self._second, self._third, self._fourth]