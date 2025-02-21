import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from DeckOfCards import DeckOfCards
from HandOfCards import HandOfCards