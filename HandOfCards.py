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

    def is_hearts(self):
        if len(self.cards) == 0:
            return False
        Hearts_Check = filter(lambda card: card.get_suit() == "H", self.cards)
        Hearts = [card.get_as_string() for card in Hearts_Check]
        return(Hearts)

    def count_points(self)
        return(reduce(lambda x, y: x+y.get_face(), self.cards, 0))


    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)
