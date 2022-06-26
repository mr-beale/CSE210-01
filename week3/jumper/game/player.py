#player
from re import X


class Jumper():
    """The brave player jumping with the parachute.
    
    The responsibility of the player is to guess the secret word before all of the lines
    on the parachute are cut.
    
    Attributes:
        freefall (bool): if the player is in freefall or not. (Freefall means game over)
        jumper (list): The ascii art that represents the Jumper's status
    """

    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._freefall = False

        self._jumper = ["          O          ",
                        "         /|\         ",
                        "         / \         ",
                        "                     ",
                        "^~^~^~^~^~^~^~^~^~^~^"]


    def get_jumper(self):
        """Gets the current ascii art for the Jumper
        
        Returns:
            list: the current ascii art
        """
        return(self._jumper)


    def is_safe(self):
        """Gets the current freefall status of the jumper
        
        Returns:
            bool: the freefall status
        """
        return self._freefall

    def _fail(self):
        """Updates the ascii art for when the parchute runs out of lines.

        Returns:
            list: the current ascii art
        """
        self._jumper = ["         \ /         ",
                        "          |          ",
                        "         /O\  SPLAT! ",
                        "^~^~^~^~^~^~^~^~^~^~^",
                        "      GAME OVER      "]

    def _victory(self):
        """Updates the ascii art for when the word is guessed correctly.
        
        Returns:
            list: the current ascii art
        """
        self._jumper = ['       __==~^~~==            ',
                        '    _==~        ~~@@==_      ',
                        '    ===  |   | ,  /  @@@@    ',
                        "    \\ \\  |   |' /  / @@@@  ",
                        '     \\ \\ |   | /  /  /  /  ',
                        "      ` \\|   |/  /  / ,'    ",
                        "      \\  |   |  / ,','      ",
                        "       \\ |   | /,' ,'       ",
                        "        \\`   ;/' ,'         ",
                        "         \\`  / ,'           ",
                        "          |o| '              ",
                        "          _@'                ",
                        '         ||                  ',
                        "        ''                   ",
                        "                             ",
                        "       SMOOTH SAILING!       ",
                        "           YOU WIN           "]

    def updateStatus(self, falling, victory):
        """Updates the current freefall status.
        Calls functions to update the ascii art
        """
        print("Hello")
        self._freefall = falling

        if not victory and falling:
            self._fail()

        if not falling and victory:
            self._victory()

    def Guess(self):
        """Prompts the user to guess a letter
        
        Returns:
            string: prompt
        """
        return("Guess a letter [A-Z]: ")

    


 