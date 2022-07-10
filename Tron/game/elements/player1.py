from game.shared.point import Point
from game.elements.player import Player
import constants

class Player1(Player):
    """
    One of two players in the game
    Responsible for controlling one of the light bikes and trying to trap the other one.

    Attributes:
        text (string): The name shown on the screen
        position (Point): Placement of the text on the screen
    """
    def __init__(self):
        """
        Creates Player 1 and sets up the lives, light cycle, and controls
        """
        super().__init__()
        #PLAYER NAME AND POSITION
        self._text = "Player 1"
        self._position = Point(10, 10)

        #REMAINING LIVES POSITION
        self.lives.set_position(Point(10, 32))

        #LIGHT BIKE COLOR, STARTING POSITION, AND STARTING VELOCITY
        self.cycle.change_color(constants.BLUE)
        self.cycle.set_position(Point(int(constants.MAX_X/2), 75))
        self.cycle.set_velocity(Point(0, constants.FONT_SIZE))
    

        #PLAYER SPECIFIC CONTROL KEYS
        self.cycle.set_player_keys(['w', 'a', 's', 'd', 'ls'])
