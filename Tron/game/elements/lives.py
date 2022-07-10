from game.elements.element import Element
from game.shared.point import Point
import constants

class Lives(Element):
    """
    Its hard to keep score in a game of sudden death. The life object represents the success of the player in their quest to not run into anything.

    Attributes:
        Text (string): The text representing the number of lives left
        font_size (int): overrides the default font size
        Color (Color): The color of the text
    """
    def __init__(self):
        """
        Creates an new instance of "Lives"
        """
        super().__init__()
        self._text = "######"
        self._font_size = 14
        self._color = constants.GREEN

    def _set_lives(self, lives):
        """
        Sets the text
        Args:
            lives (string): the text we want to use to represent the lives
        """
        self._text = lives

    def update_lives(self):
        """
        Removes lives and updates the text as the player runs into things

        Returns:
            bool: representing if the player is out of lives yet or not
        """
        text = self.get_text()
        number = len(text)
        number -= 1
        if number >= 0:
            self._set_lives(text[0:number])
            self.set_position(Point(self.get_position().get_x() + self._font_size, self.get_position().get_y()))

        if number == 2: self._color = constants.YELLOW
        if number == 1: self._color = constants.RED

        if len(text) == 0:
            return(True)
        else:
            return(False)