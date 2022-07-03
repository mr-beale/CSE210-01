from pyray import *

class VideoService():
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 

    Attributes:
        caption (string): The name of the window
        width (int): the widht of the window
        height (int): The height of the window
        frame_rate (int) the target framrate of the animation
    """

    def __init__(self):
        """Constructs a new VideoService using the specified debug mode."""
        self._caption = "Greed"
        self._width = 800
        self._height = 450
        self._frame_rate = 60
        
    def exit(self):
        """Closes the window and releases all computing resources."""
        close_window()

    def start_drawing(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        begin_drawing()
        clear_background(BLACK)

    def draw_object(self, object):
        """Draws the given object on the screen.
        Args:
            object (Object): the object to draw"""
        text = object.get_text()
        x = object.get_x()
        y = object.get_y()
        size = object.get_size()
        color = object.get_color()

        draw_text(text, x, y, size, color)
        object.move()

    def draw_objects(self, objects):
        """Draws the objects in the given list
        Args:
            objects (list) a list of objects to draw
        """
        for object in objects:
            self.draw_object(object)

    def stop_drawing(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        end_drawing()

    def running(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        init_window(self._width, self._height, self._caption)
        set_target_fps(self._frame_rate)

    def window_size(self):
        """Gets the video screen's width and height"""
        return(self._width, self._height)