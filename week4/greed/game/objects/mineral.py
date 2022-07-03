from random import randint, randrange
from game.objects.object import Object

class Mineral(Object):
    """A general classification for stony type objects, valuable or otherwise.
    
    Attributes:
        Inherits methods from Object
        x (int): a value representing the X coordinate
        y (int): a value representing the Y coordinate
        speed (int): a vlue dictating how quickly the item falls
        size (int): The font size of the object's text

    """
    def __init__(self):
        """Constructs a new Mineral and inherits methods from Object.
        
        Args:
            self (Mineral): an instance of Mineral
        """

        self._x = randrange(10, 801, 20)
        self._y = randint(-100, 0)
        self._speed = randint(1,7)
        self._size = randint(20, 26)

    def move(self):
        """Updates the objects y coordinate by the speed to animate the falling
        Args:
            self (Mineral): an instance of Mineral
        """
        self._y += self._speed

    def get_value(self):
        """Returns the point value of the object to calculate the total score
        Args:
            self (Mineral): an instance of Mineral
        """
        return(self._points)


