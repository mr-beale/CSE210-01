#parachute
class Parachute():
    """The parachute that may or may not fail
    
    The responsibility of the parachute is to keep the jumper safe...
    how well it does that depends on how well the jumper is at guessing

    Creates the ascii art for the parachute and tracks how many attempts are remaining until the game is over
    
    Attributes:
        chute (list): A list of lines creating the ascii art to display the parachute
    """

    def __init__(self):
        """Constructs a new Parachute.
        
        Args:
            self (Parachute): an instance of Parachute.
        """
        self._chute = ["         ___         ",
                       "      .-'   '-.      ",
                       "     /         \     ",
                       "     \^^^^|^^^^/     ",
                       "      \   |   /      ",
                       "       \  |  /       ",
                       "        \ | /        ",
                       "         \|/         ",]

    def get_chute(self):
        """Gets the current ascii art to display the parachute
        Returns:
            list: the ascii art for the parachute
        """
        return(self._chute)

    def cut_line(self):
        """Removes the first entry from the ascii art list
        
        Returns:
            list: the modified ascii art"""
        try:
            self._chute.pop(0)
        except IndexError:
            return
