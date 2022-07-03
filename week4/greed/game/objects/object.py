class Object():
    """An object to be renered in the window
       Contains universal methods to be used by its children
    
    Attributes:
        none
    """
    def __init__(self):
        """Constructs a new object
        
        Args:
            self (Object): An instance of Object
        """
        pass

    def get_text(self):
        """Gets the text to be displayed in the window
        Args:
            self (Object): An instance of Object
        """
        return(self._text)

    def get_x(self):
        """Gets the objects X coordinate
        Args:
            self (Object): An instance of Object
        """
        return(self._x)

    def get_y(self):
        """Gets the objects Y coordinate
        Args:
            self (Object): An instance of Object
        """
        return(self._y)

    def get_size(self):
        """Gets the objects font size
        Args:
            self (Object): An instance of Object
        """
        return(self._size)
    
    def get_color(self):
        """Gets the objects font color
        Args:
            self (Object): An instance of Object
        """
        return(self._color)