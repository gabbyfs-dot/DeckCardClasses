class Card:


 def __init__(self, rank="Ace", suit="Spades"):
    self.rank = rank
    self.suit = suit

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