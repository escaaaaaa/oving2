import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from src.DeckOfCards import DeckOfCards


#Check if the deck is created with 52 cards
class TestDeckOfCards(unittest.TestCase):
    def test_deck_init(self):
        deck=DeckOfCards()
        self.assertEqual(len(deck.cards), 52) 

#Check if the hand is dealt 5 cards
    def test_deal_hand(self):
        deck = DeckOfCards()
        hand = deck.deal_hand(5)
        self.assertEqual(len(hand.cards), 5)

#Check if dealing more cards than are in the deck raises an error
    def test_deal_hand_too_many_cards(self):
        deck = DeckOfCards()
        with self.assertRaises(ValueError):
            deck.deal_hand(53)

#Check to see if all the cards dealt are unique, and no longer in the deck
    def test_deal_hand_unique_cards(self):
        deck = DeckOfCards()
        hand = deck.deal_hand(5)
        for card in hand.cards:
            self.assertNotIn(card, deck.cards)

#Check that the hand dealt is a string representation, and not empty
    def test_str_representation(self):
        deck = DeckOfCards()
        deck_str = str(deck)
        self.assertIsInstance(deck_str, str)  # Check if the output is a string
        self.assertGreater(len(deck_str), 0)

if __name__ == "__main__":
    unittest.main()
