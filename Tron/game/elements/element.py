import constants
from game.shared.point import Point

class Element():
    """
        A graphical element of the game.

        Attributes:
            font_size (int): size of the element
            color (Color): color of the element
            velocity (Point): speed and direction of the element
            text (string): text representing the element
            position (Point): the position of the element on the screen
    """
    def __init__(self):
        self._font_size = 20
        self._color = constants.WHITE
        self._velocity = Point(0, 0)
        self._text = ""
        self._position = Point(0, 0)

    def set_position(self, new):
        """
            Updates the position of the current element
            Args:
                new (point): the new position
        """
        self._position = new
    
    def get_position(self):
        """
            Gets the position of the element
            Returns:
                position (Point): The current position
        """
        return(self._position)

    def get_text(self):
        """
            Gets the text of the element
            Returns:
                text (String): The current text
        """

        return(self._text)
    
    def set_text(self, text):
        """
            Updates the text of the current element
            Args:
                text (string): the new text
        """
        self._text = text

    def get_font_size(self):
        """
            Gets the font size of the element
            Returns:
                font_size (int): The current font size
        """
        return(self._font_size)

    def get_color(self):
        """
            Gets the color of the element
            Returns:
                color (Color): The current color
        """
        return(self._color)
    
    def change_color(self, color):
        """
            Updates the color of the current element
            Args:
                color (Color): the new color
        """
        self._color = color

    def get_size(self):
        """
            Gets the size of the element
            Returns:
                width (int): The size in the x axis
                height (int): The size in the y axis
        """
        return(self._width, self._height)

    def set_size(self, width, height):
        """
            Updates the size of the current element
            Args:
                width (int): the new dimension in the x axis
                height (int): the new dimension in the y axis
        """
        self._width = width
        self._height = height

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self):
        """This function is defined by the child class"""
        pass