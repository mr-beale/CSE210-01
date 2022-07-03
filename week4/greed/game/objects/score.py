from game.objects.object import Object
from pyray import WHITE

class Score(Object):
    """The total number of points earned during the game

    Attributes:
        score (int) the points earned
        x (int) The x coordinate of the text location in the window
        y (int) The Y coordinate of the text location in teh window
        color (pyray color): The color of the font
        size (int): The font size
    """
    def __init__(self):
        """Constructs a new instance of Score and inherits methods from Object
        
        Args:
            self (Score): An instance of Score
        """
        self._score = 0
        self._x = 5
        self._y = 5
        self._color = WHITE
        self._text = f"SCORE: {self._score}"
        self._size = 25

    def add(self, points):
        """Adds the point value of a caught mineral to the total score
        Args:
            self (Score): An instance of Score
            points (int): The point value of the mineral caught by the player
        """
        self._score += points
        self._text = f"SCORE: {self._score}"

    def move(self):
        """To reduce lines of code, the "Move" funciton for the
        minerals and player are called in draw_object function of the video service
        This function the Score object to be drawn by that function as well without
        error
        
        Args:
            self (Score): An instance of Score
        """
        pass

