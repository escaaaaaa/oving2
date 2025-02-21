import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PlayingCard import PlayingCard


class TestPlayingCard(unittest.TestCase):

    #Test that a card is initialized correctly when given valid inputs
    def test_valid_initialization(self):
        card = PlayingCard("H", 10)  # 10 of Hearts
        self.assertEqual(card.get_suit(), "H")
        self.assertEqual(card.get_face(), 10)

    #Test that an invalid suid creates an error
    def test_invalid_suit_initialization(self):
        with self.assertRaises(ValueError):
            PlayingCard("X", 10)  # Invalid suit

    #Test that an invalid number creates an error
    def test_invalid_face_initialization(self):
        with self.assertRaises(ValueError):
            PlayingCard("H", 14)  # Invalid face

    #Test that it strings correctly
    def test_get_as_string(self):
        card = PlayingCard("H", 10)  # 10 of Hearts
        self.assertEqual(card.get_as_string(), "H10")

    #Test that get_suit() returns the correc suit
    def test_get_suit(self):
        card = PlayingCard("D", 5)  # 5 of Diamonds
        self.assertEqual(card.get_suit(), "D")

    #Test that get_face() returns the correct value
    def test_get_face(self):
        card = PlayingCard("S", 12)  # Queen of Spades
        self.assertEqual(card.get_face(), 12)

    #Testing two identical cards are in fact equal
    def test_equality(self):
        card1 = PlayingCard("H", 10)  # 10 of Hearts
        card2 = PlayingCard("H", 10)  # 10 of Hearts
        card3 = PlayingCard("D", 10)  # 10 of Diamonds
        self.assertEqual(card1, card2)  # Same suit and face
        self.assertNotEqual(card1, card3)  # Different suit

    #Testing the hash of a card
    def test_hash(self):
        card1 = PlayingCard("H", 10)  # 10 of Hearts
        card2 = PlayingCard("H", 10)  # 10 of Hearts
        card3 = PlayingCard("D", 10)  # 10 of Diamonds
        self.assertEqual(hash(card1), hash(card2))  # Same suit and face
        self.assertNotEqual(hash(card1), hash(card3))  # Different suit

if __name__ == "__main__":
    unittest.main()