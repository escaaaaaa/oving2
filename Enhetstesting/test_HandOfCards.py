import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

#A test-set of cards
cards = [
    PlayingCard("H", 10),  # 10 of Hearts
    PlayingCard("D", 11),   # Jack of Diamonds
    PlayingCard("S", 12),   # Queen of Spades
    PlayingCard("C", 13),   # King of Clubs
    PlayingCard("H", 1)    # Ace of Hearts
    ]

#Test that the hand is initialized with a correct number of cards, correctly
class TestHandOfCards(unittest.TestCase):
    def test_hand_initialization(self):
        hand = HandOfCards(cards)
        self.assertEqual(len(hand.cards), 5)

#Test that it actually catches a flush
    def test_is_flush_true(self):
        flush_cards = [
            PlayingCard("H", 10),  # 10 of Hearts
            PlayingCard("H", 11),   # Jack of Hearts
            PlayingCard("H", 12),   # Queen of Hearts
            PlayingCard("H", 13),   # King of Hearts
            PlayingCard("H", 1)    # Ace of Hearts
        ]
        hand = HandOfCards(flush_cards)
        self.assertTrue(hand.is_flush()) 

#Test that it returns false when it is not a flush
    def test_is_flush_false(self):
        hand = HandOfCards(cards)
        self.assertFalse(hand.is_flush()) 

#Test for the "return Heart cards" function to see if it returns the correct cards       
    def test_is_hearts_with_hearts(self):
        hand = HandOfCards(cards)
        self.assertEqual(hand.is_hearts(), "H10 H1")

#Test for a False result when there are no Hearts
    def test_is_hearts_no_hearts(self):
        no_heart_cards = [
            PlayingCard("C", 10),  # 10 of Hearts
            PlayingCard("D", 11),   # Jack of Diamonds
            PlayingCard("S", 12),   # Queen of Spades
            PlayingCard("C", 13),   # King of Clubs
            PlayingCard("D", 1)    # Ace of Hearts
            ]
        hand = HandOfCards(no_heart_cards)
        self.assertFalse(hand.is_hearts()) 

#Test that it counts the points correctly
    def test_count_points(self):
        hand = HandOfCards(cards)
        self.assertEqual(hand.count_points(), 47)

#Test that it correctly identifies the Queen of spades
    def test_is_ladyspade_true(self):
        hand = HandOfCards(cards)
        self.assertTrue(hand.is_ladyspade())

#Test that it correctly identifies the lack of the Queen of spades
    def test_is_ladyspade_false(self):
        cards = [
            PlayingCard("H", 10),  # 10 of Hearts
            PlayingCard("D", 11),   # Jack of Diamonds
            PlayingCard("D", 12),   # Queen of Spades
            PlayingCard("C", 13),   # King of Clubs
            PlayingCard("H", 1)    # Ace of Hearts
            ]
        hand = HandOfCards(cards)
        self.assertFalse(hand.is_ladyspade()) 

#Test that the string representation of the hand is ok
    def test_str_representation(self):
        hand = HandOfCards(cards)
        self.assertEqual(str(hand), "H10, D11, S12, C13, H1")  # Check the string representation

if __name__ == "__main__":
    unittest.main()