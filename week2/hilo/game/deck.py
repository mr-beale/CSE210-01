class Card():
    """Holds the information for an individual card in a deck

       Attributes:
        value - the number value of the card (1-13)
        suit - the face suit of the card (heart, diamond, club, or spade)
    """

    def __init__(self):
        """Constructs a new card
           Args: self - an instance of "card"
        """

        self.value = 0
        self.suit = None
    
class Deck():
    """A deck containing 52 unique cards
    
        Attributes:
            cards - a list containing the cards that make up the deck
    """

    def __init__(self, ):
        """Constructs a new deck
           Args: self - an instance of "Deck"
        """
        self.cards = []

        self.createDeck()

    def createDeck(self):
        """Generates a list of 52 cards.
           There are 4 suits each with cards valued from 1-13
        """
        
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for i in range(1,14):
                card = Card()
                card.value = i
                card.suit = suit
                self.cards.append(card)