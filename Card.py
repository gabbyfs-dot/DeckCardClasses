class Card:
    """
    Represents a single playing card (rank + suit).
    Owns a dictionary mapping ranks -> point values (as required).
    """

# dictionary of ranks and point values (REQUIRED)
rank_points = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
    }

def __init__(self, rank="Ace", suit="Spades"):
    self.rank = rank
    self.suit = suit

    # Big 3
def __str__(self):
    return self.rank + " of " + self.suit

def __repr__(self):
    return "Card('" + self.rank + "', '" + self.suit + "')"

def __eq__(self, other):
    if type(other) == Card:
        return self.rank == other.rank and self.suit == other.suit
    if type(other) == int:
        return Card.rank_points[self.rank] == other
        return False