# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_card.ipynb.

# %% ../00_card.ipynb 3
from __future__ import print_function, division

import random


class Card:
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other) -> bool:
        """Checks whether self and other have the same rank and suit.
        """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other) -> bool:
        """Compares this card to other, first by suit, then rank.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
    def __repr__(self): return self.__str__()
    
    def foo(): pass

# %% auto 0
__all__ = ['Card']
