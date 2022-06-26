import random

class SecretWord():
    """The word beign guessed. 
    
    The responsibility of a SecretWord is to be sneaky and secretive
    
    Attributes:
        word (string): one of 50 words chosen randomly
        guessed (list): list of letters already guessed by the player
    """
    def __init__(self):
        """Constructs a new SecretWord
        
        Args:
            self (SecretWord): An instance of SecretWord
        """

        rw = RandomWord()
        self._word = rw.random_word()
        self.guessed = []
        print(self._word)


    def goodGuess(self):
        """Determines weather or not the guessed letter is in the secret word
        
        Returns:
            bool: yes or no
        """

        if self.guessed[-1] in self._word:
            return True
        else:
            return False

    def show_word(self):
        """Creates the masked version of the secret word
        
        Returns:
            string: the masked word
        """
        masked = ""
        for i in range(0, len(self._word)):
            if self._word[i] in self.guessed:
                masked += (self._word[i].upper()+" ")
            else:
                masked += ("_ ")
        return(masked)


    def Guessed(self, unmasked):
        """Determines if the word has been correctly guessed or not
        
        Returns:
            bool: yes or no
        """
        unmasked = unmasked.split(" ")
        word = "".join(unmasked)
        if word.lower() == self._word:
            return True
        else:
            return False

class RandomWord():
    """A randomly chosen word 

    Attributes:
        words (list): a list of 50 words that can be chosen
    """
    def __init__(self):
        """Constructs a new RandomWord
        
        Args:
            self (RandomWord): An instance of RandomWord
        """
        self.__words = ['buttocks',
                        'dictionary',
                        'housing',
                        'company',
                        'dress',
                        'choke',
                        'stick',
                        'grave',
                        'process',
                        'clean',
                        'rugby',
                        'inject',
                        'hypnothize',
                        'bland',
                        'emphasis',
                        'bacon',
                        'temptation',
                        'leader',
                        'rally',
                        'quality',
                        'continental',
                        'temporary',
                        'bathroom',
                        'print',
                        'population',
                        'refund',
                        'throw',
                        'civilization',
                        'smile',
                        'sample',
                        'restoration',
                        'strap',
                        'surgeon',
                        'compound',
                        'study',
                        'review',
                        'expect',
                        'agree',
                        'track',
                        'instruction',
                        'angle',
                        'forge',
                        'sharp',
                        'illustrate',
                        'absorption',
                        'remember',
                        'trial',
                        'civilian',
                        'temple',
                        'salvation']

    def random_word(self):
        """Chooses a word from the list at random
        Retruns:
            string: A random word
        """
        word = random.choice(self.__words)

        return(word)