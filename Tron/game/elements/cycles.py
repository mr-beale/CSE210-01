from game.services.keyboard_service import KeyboardService
from game.elements.element import Element
from game.shared.point import Point
import constants

class Cycle(Element):
    """
        A Colorful bike that leaves a trail of blinding light behid it
        This is the interactive element of the game. Responsible for 
        moving and not running into things

        Attributes:
        width (int): width of the trail
        height (int): height of an individual section of trail
        keys (KeyboardService): service to allow keyboard input
        player_keys (list): list of keys accessable by a particular instance
        speed (int): the rate at wich the cycle moves
        trail_behind (list): A list containing all of the points the cycle has prevoiusly crossed.
    """
    def __init__(self):
        """
        Creates a new instance of Cycle
        """
        super().__init__()
        self._width = constants.FONT_SIZE
        self._height = constants.FONT_SIZE
        self._keys = KeyboardService()
        self._player_keys = []
        self._speed = constants.FONT_SIZE

        self._trail_behind = []

    def get_trail(self):
        """
        Gets the current list of trailing elements
        Returns:
            trail_behind
        """
        return(self._trail_behind)

    def set_player_keys(self, keys):
        """
        Sets the keys that can control this particular cycle
        Args:
            keys (list)
        """
        self._player_keys = keys

    
    def move_next(self):
        """
            Sets the position that the cycle should move to next.
            The elements will wrap around the screen when they exceed the max limits
        """
        self._trail_behind.append(self.get_position())
        self._get_direction()

        x = (self.get_position().get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self.get_position().get_y() + self._velocity.get_y()) % constants.MAX_Y
        self.set_position(Point(x, y))

    def _get_direction(self):
        """
            Defines the direction that the cycle should be moving in.
            Does not allow the user to travel backward on top of their trail
        """
        new_velocity = self.get_velocity()
    
        if self._keys.is_key_down(self._player_keys[0]):
            new_velocity = Point(0, -self._speed)
        if self._keys.is_key_down(self._player_keys[1]):
            new_velocity = Point(-self._speed, 0)
        if self._keys.is_key_down(self._player_keys[2]):
            new_velocity = Point(0, self._speed)
        if self._keys.is_key_down(self._player_keys[3]):
            new_velocity = Point(self._speed, 0)
        if self._keys.is_key_down(self._player_keys[4]):
            self._speed = int(constants.FONT_SIZE /2)

        if not (abs(self.get_velocity().get_x()) == abs(new_velocity.get_x()))\
        and not (abs(self.get_velocity().get_y()) == abs(new_velocity.get_y())):
            self.set_velocity(new_velocity)