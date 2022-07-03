from random import choice
from game.objects.gem import Gem
from game.objects.rock import Rock

class Minerals():
    """An object containing a list of constructed mineral objects
    
    Arttributes:
        minerals (list): The list of created minerals
    """
    def __init__(self):
        """Constructs 50 new mineral objects and appends them to the minerals list
        Args:
            self (Minerals): an instance of Minerals
        """
        self._minerals = []
        for i in range(0, 50):
            mineral = choice([Gem(), Rock()])
            self._minerals.append(mineral)

    def replace(self, old):
        """Removes a mineral from the list and constructs a new Mineral to take its place.
        Args:
            self (Minerals): an instance of Minerals
            old (Mineral) an instance of the Mineral object
        """
        self._minerals.remove(old)

        new = choice([Gem(), Rock()])

        self._minerals.append(new)

    def get_objects(self):
        """Returns the current list of Minerals
        Args:
            self (Minerals): an instance of Minerals
        """
        return(self._minerals)