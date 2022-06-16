import random

from game.deck import Deck
from game.player import Player

class Dealer():
    """Responsible for dealing the cards and calculating the players score.

    Attributes:
        playedCards - A list of all of the cards that have already been flipped.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self - an instance of Director.
        """

        self.playedCards = []

        self.deck = Deck()
        self.player = Player()

    def flipCard(self):
        """
            Pulls a random card from the Deck and appends it to the list of played cards.
        """
        card = random.choice(self.deck.cards)
        self.playedCards.append(card)
        self.deck.cards.remove(card)

    def addPoints(self):
        """
            Calculates the players current score. If they guess right they get 100 points
            If they guess wrong they lose 75 points.
        """
        if (self.thisCard.value > self.nextCard.value and self.player.guess == "l") or \
           (self.thisCard.value < self.nextCard.value and self.player.guess == "h"):
            self.player.points += 100
        else:
            self.player.points -= 75
            if self.player.points < 0: self.player.points = 0
        
        print(f'Your score is: {self.player.points}')


    def playRound(self):
        """
            Runs the main loop for a round of the game.
            The loop ends when the player decides not to play aonther round
            or when their score reaches 0.
        """

        while self.player.playing == True:
            self.flipCard()
            self.thisCard = self.playedCards[-2]
            print(f'\nThe card is: {self.thisCard.value} of {self.thisCard.suit}')

            self.player.makeGuess()
            self.nextCard = self.playedCards[-1]
            print(f'Next card was: {self.nextCard.value} of {self.nextCard.suit}')

            self.addPoints()
            self.player.playAgain()

        print("\nGame over!")
        print("Thanks for playing.")
