from functools import reduce

class HandOfCards:
    """
    A class to represent a hand of playing cards.
    Attributes:
    -----------
    cards : list
        A list of card objects representing the hand.
    Methods:
    --------
    is_flush():
        Checks if all cards in the hand have the same suit.
    __str__():
        Returns a string representation of the hand of cards.
    """
    def __init__(self, cards):
        """
        Initializes a HandOfCards instance.

        Args:
            cards (list): A list of card objects that make up the hand.
        """
        self.cards = cards

    def is_flush(self):
        if len(self.cards) < 5:
            return False
        first_suit = self.cards[0].get_suit()
        return all(card.get_suit() == first_suit for card in self.cards)

        #Below there be dragons (I wrote the code myself before __str__)

    #Checking for any hearts and returning them if there are any
    def is_hearts(self):
        if len(self.cards) == 0:
            return False
        Hearts_Check = filter(lambda card: card.get_suit() == "H", self.cards)
        Hearts = [card.get_as_string() for card in Hearts_Check]
        return " ".join(Hearts) if Hearts else False

    #Counts the total number value of the cards
    def count_points(self):
        return(reduce(lambda x, y: x+y.get_face(), self.cards, 0))

    #Checks if there is a queen of spades in the hand
    def is_ladyspade(self):
        for card in self.cards:
            if card.get_as_string() == "S12":
                return True
        return False


    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)
