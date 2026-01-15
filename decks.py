
import random

class Deck:

       ranks_and_values = [
        ("Two", 2),
        ("Three", 3),
        ("Four", 4),
        ("Five", 5),
        ("Six", 6),
        ("Seven", 7),
        ("Eight", 8),
        ("Nine", 9),
        ("Ten", 10),
        ("Jack", 10),
        ("Queen", 10),
        ("King", 10),
        ("Ace", 11)
    ]

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

def __init__(self):
        self.cards = []
        self.build_deck()

def __str__(self):
        return "Deck with " + str(len(self.cards)) + " cards"

def __repr__(self):
        return "Deck(" + str(len(self.cards)) + " cards)"

def __eq__(self, other):
    return self.cards == other.cards

def build_deck(self):
        self.cards = []
        for suit in Deck.suits:
            for rank, value in Deck.ranks_and_values:
                self.cards.append((rank, suit))

def shuffle(self):
    random.shuffle(self.cards)

def draw(self):
        """Remove and return one card from the deck."""
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
