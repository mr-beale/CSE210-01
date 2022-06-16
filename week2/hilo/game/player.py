class Player():
    """Represents an individual playing the game.
       Responsible for making guesses, tracking their points,
       and deciding if they are going to continue playing
       
       Attributes:
        guess - weather or not they think the next card will be high or low
        points - total points earned by the player
        playing - weather or not the player wants to play another round
    """

    def __init__(self):
        """Constructs a new player
           Args: self - an instance of "Player"
        """

        self.guess = ""
        self.points = 300
        self.playing = True

    def makeGuess(self):
        """Gets the players guess from the console input.
           Args: self - an instance of "Player
        """

        self.guess = input("Higher or Lower? (h/l) ")
        while self.guess.lower() != "h" and self.guess.lower() != "l":
            print(f'\n{self.guess} is not a valid option.')
            self.guess = input("Higher or Lower? (h/l) ")

    def playAgain(self):
        """Allows the player to decide if the want to play another round.
           Ends the game if the players score reaches 0.
        """
        if self.points == 0: self.playing = False
        else:
            choice = input("Play again? (y/n) ")
            while choice.lower() != "y" and choice.lower() != "n":
                print(f'\n{choice} is not a valid option.')
                choice = input("Play again? (y/n) ")
            if choice.lower() == "y": self.playing = True
            elif choice.lower() == "n": self.playing = False