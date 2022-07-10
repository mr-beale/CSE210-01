from game.elements.player1 import Player1
from game.elements.player2 import Player2
from game.services.video_service import VideoService
from game.elements.boundaries import Wall
from game.shared.point import Point
from game.elements.element import Element
import constants

class Game():
    """
        The main body of the game. Its responsible for making all of the other things work
    """
    def __init__(self):
        """
        Creates a new instance of Game
        """
        
        player2 = Player2()
        player1 = Player1()
        
        left = Wall(20, constants.MAX_Y - 50, Point(0, 50), constants.WHITE)
        right = Wall(20, constants.MAX_Y - 50, Point(constants.MAX_X - 20, 50), constants.WHITE)
        top = Wall(constants.MAX_X, 20, Point(0, 50), constants.WHITE)
        bottom = Wall(constants.MAX_X, 20, Point(0, constants.MAX_Y - 20), constants.WHITE)
        banner = Wall(constants.MAX_X, 50, Point(0, 0), constants.GRAY)

        self._is_game_over = False
        self.players = [player1, player2]
        self.borders = [left, right, top, bottom, banner]
        self.elements = []

        for player in self.players:
            self.borders.append(player.lives)
            self.elements.append(player.cycle)

        self.vs = VideoService(True)

    def run(self):
        """
        Starts the main loop"""
        self.vs.open_window()
        while self.vs.is_window_open():
            self.vs.clear_buffer()
            self.status(self.players)
            self.vs.draw_actors(self.elements)
            self.vs.draw_actors(self.borders)
            self.vs.draw_actors(self.players)
            self.vs.flush_buffer()
        self.vs.close_window

    def status(self, players):
        """
        Listens for the status of the game to change
        
        Agrs:
            players (list): list of players in the game
        """
        self._handle_collisions(players)
        self._handle_game_over(players)

    def _handle_collisions(self, players):
        """Sets the game over flag if either of the light bikes collide with any other element on the screen
        
        Args:
            players (list): list of players in the game
        """
        self._intersecting(players)
        self._self_intersecting(players)
        self._ran_into_wall(players)

    def _intersecting(self, players):
        """Sets the game over flag if a light bike intersects with the trail of the other
        
        Args:
            players (list): list of players in the game
        """
        player1 = players[0]
        player2 = players[1]
        for point in player1.cycle.get_trail():
            if player2.cycle.get_position().equals(point):
                self._is_game_over = player2.lives.update_lives()
    
        for point in player2.cycle.get_trail():
            if player1.cycle.get_position().equals(point):
                self._is_game_over = player1.lives.update_lives()

    def _self_intersecting(self, players):
        """Sets the game over flag if a light bike intersects its own trail
        
        Args:
            players (list): list of players in the game
        """
        for player in players:
            for point in player.cycle.get_trail():
                if player.cycle.get_position().equals(point):
                    self._is_game_over = player.lives.update_lives()

    def _ran_into_wall(self, players):
        """Sets the game over flag if either of the light bikes hits the barries around the playing area
        
        Args:
            players (list): list of players in the game
        """
        for player in players:
            cycle = player.cycle.get_position()
            if cycle.get_x() < 20\
            or cycle.get_x() > constants.MAX_X -20\
            or cycle.get_y() < 70\
            or cycle.get_y() > constants.MAX_Y -20:
                self._is_game_over = player.lives.update_lives()
        
    def _handle_game_over(self, players):
        """Shows the 'game over' message and turns the light bikes white if the game is over.
        
        Args:
            players (list): list of players in the game
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)-50
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Element()
            message.set_text("Game Over!")
            message.set_position(position)
            self.elements.append(message)
            message.change_color(constants.GREEN)

            for player in players:
                player.cycle.change_color(constants.WHITE)