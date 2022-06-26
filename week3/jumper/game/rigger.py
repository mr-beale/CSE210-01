from game.term import Term
from game.player import Jumper
from game.parachute import Parachute
from game.secret_word import SecretWord


class Rigger():
    """A rigger is a person who prepares parachutes..
    
    The responsibility of the rigger object is to direct the gameplay.

    Attributes:
        chute (Parachute): The players parachute (lives left)
        player (Jumper): The person playing the game
        word (SecretWord): The word to be guessed
        terminal (Term): Gets input from and sends output to the terminal
    """

    def __init__(self):
        """Constructs a new Rigger.
        
        Args:
            self (Rigger): an instance of Rigger.
        """
        self._terminal = Term()
        self._word = SecretWord()
        self._Player = Jumper()
        self._chute = Parachute()

    def playRound(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Rigger): an instance of Rigger.
        """  

        while not self._Player.is_safe():
            self._do_outputs()
            self._do_inputs()
            self._do_updates()

        self._do_outputs()

    def _do_inputs(self):
        """The player guesses a letter

        Args:
            self (Rigger): An instance of Rigger.
        """
        guess = self._terminal.Input(self._Player.Guess())
        self._word.guessed.append(guess.lower())

    def _do_updates(self):
        """Monitors the safety of the jumper.
        
        Args:
            self (Rigger): An instance of Rigger
        """
        if self._word.goodGuess() == False: self._chute.cut_line()

        if len(self._chute.get_chute()) == 0:
            print()
            falling = True
            victory = False
        
            self._Player.updateStatus(falling, victory)

        if self._word.Guessed(self._word.show_word()):
            falling = False
            victory = True

            self._chute.get_chute().clear()

            self._Player.updateStatus(falling, victory)

        self._Player.is_safe()

    def _do_outputs(self):
        """Shows a masked version of the secret word and draws the jumper and the parachute"""
        print()
        self._terminal.Output(self._word.show_word())
        print()
        self._terminal.asciiArt(self._chute.get_chute())
        self._terminal.asciiArt(self._Player.get_jumper())
        print()