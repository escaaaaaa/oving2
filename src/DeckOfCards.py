from PlayingCard import PlayingCard
from HandOfCards import HandOfCards
import random


class DeckOfCards:
    """
    A class to represent a deck of playing cards.
    Attributes
    ----------
    cards : list
        A list of PlayingCard objects representing the deck.
    Methods
    -------
    __init__():
        Initializes the deck with 52 playing cards.
    deal_hand(n):
        Deals a hand of 'n' cards from the deck.
    __str__():
        Returns a string representation of the deck.
    """
    def __init__(self):
        """
        Initializes a new deck of cards.

        The deck consists of 52 cards, with each card having a suit from the list 
        ['S', 'H', 'D', 'C'] (Spades, Hearts, Diamonds, Clubs) and a face value 
        ranging from 1 to 13.

        Attributes:
            cards (list): A list of PlayingCard objects representing the deck.
        """
        suits = ['S', 'H', 'D', 'C']
        self.cards = [PlayingCard(suit, face) for suit in suits for face in range(1, 14)]

    def deal_hand(self, n):
        """
        Deals a hand of n cards from the deck.

        Parameters:
        n (int): The number of cards to deal. Must be between 1 and 52 inclusive.

        Returns:
        HandOfCards: An instance of HandOfCards containing the dealt cards.

        Raises:
        ValueError: If n is not between 1 and 52 inclusive.
        """
        if not (1 <= n <= 52):
            raise ValueError("Parameter n must be a number between 1 and 52")
        hand_cards = random.sample(self.cards, n)
        return HandOfCards(hand_cards)


    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)
