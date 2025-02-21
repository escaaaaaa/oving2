class PlayingCard:
    """
    A class to represent a playing card.
    Attributes:
        suit (str): The suit of the card, which must be one of 'H' (Hearts), 'D' (Diamonds), 'C' (Clubs), or 'S' (Spades).
        face (int): The face value of the card, which must be an integer between 1 and 13.
    Methods:
        __init__(suit, face):
            Initializes the PlayingCard with a suit and a face value.
        get_as_string():
            Returns the string representation of the card in the format "suitface".
        get_suit():
            Returns the suit of the card.
        get_face():
            Returns the face value of the card.
        __eq__(other):
            Checks if this card is equal to another card based on suit and face value.
        __hash__():
            Returns the hash value of the card based on its suit and face value.
    """
    def __init__(self, suit, face):
        """
        Initialize a PlayingCard object.
        Parameters:
        suit (str): The suit of the card, must be one of 'H' (Hearts), 'D' (Diamonds), 'C' (Clubs), or 'S' (Spades).
        face (int): The face value of the card, must be a number between 1 and 13.
        Raises:
        ValueError: If the suit is not one of 'H', 'D', 'C', or 'S'.
        ValueError: If the face is not a number between 1 and 13.
        """
        if suit not in ['H', 'D', 'C', 'S']:
            raise ValueError("Parameter suit must be one of H, D, C or S")
        if not (1 <= face <= 13):
            raise ValueError("Parameter face must be a number between 1 to 13")
        
        self.suit = suit
        self.face = face

    def get_as_string(self):
        
        return f"{self.suit}{self.face}"

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face

    def __eq__(self, other):
        if isinstance(other, PlayingCard):
            return self.suit == other.suit and self.face == other.face
        return False

    def __hash__(self):
        return hash((self.suit, self.face))