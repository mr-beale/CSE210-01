from game.objects.minerals import Minerals
from game.objects.score import Score
from game.objects.player import Player
from game.services.videoService import VideoService

class Greed():
    """A Entity that keeps the game running. 
    
    The responsibility of this is to control the sequence of play.

    Attributes:
            score (Score): for storing and updating the players socre
            player (Player): to provide the player with keyboard input and a character on the screen
            vs (VideoService): for providing video output.
            minerals (Minerals): for rendering the falling objects in the window
            items (list) :to hold a list of many objects to show in the window
    """
    def __init__(self):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            self (Greed) An instance of Greed
        """
        self._vs = VideoService()

        self._minerals = Minerals()
        self._items = self._minerals.get_objects()
        self._player = Player()
        self._score = Score()

    def main_loop(self):
        """Starts the game. Runs the main game loop.

        Args:
            self (Greed): An instance of Greed.
        """
        self._vs.open_window()
        while self._vs.running():
            self._get_inputs()
            self._do_updates()
            self._do_output()
        self._vs.exit()

    def _get_inputs(self):
        """Gets directional input from the keyboard and applies it to the Player.
        
        Args:
            self (Greed): An instance of Greed.
        """
        self._vs.start_drawing()
        self._vs.draw_object(self._player)

    def _do_updates(self):
        """Updates the Players's position and resolves any collisions with minerals.
        
        Args:
            self (Greed): An instance of Greed.
        """
        width, height = self._vs.window_size()
        for item in self._items:
            if self._player.get_x() in range(item.get_x()-10, item.get_x()+10) and self._player.get_y() in range(item.get_y()-10, item.get_y()+10):
                score = item.get_value()
                self._minerals.replace(item)
                self._score.add(score)

            if item.get_y() > height:
                self._minerals.replace(item)

    def _do_output(self):
        """Draws the objects on the screen.
        
        Args:
            self (Greed): An instance of Greed.
        """
        self._vs.draw_object(self._score)
        self._vs.draw_objects(self._items)
        self._vs.stop_drawing()