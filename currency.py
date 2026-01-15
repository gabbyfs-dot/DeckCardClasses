class Currency:
    
    def __init__(self, amount=0.0, code="USD"):
        self.amount = float(amount)
        self.code = code

    def __str__(self):
        return str(self.amount) + " " + self.code

    def __repr__(self):
        return "Currency(" + str(self.amount) + ", '" + self.code + "')"


    def __mul__(self, other):
        return Currency(self.amount * other, self.code)

    def __truediv__(self, other):
        return Currency(self.amount / other, self.code)

    def __iadd__(self, other):
            if self.code == other.code:
             self.amount += other.amount
             return self

    def __isub__(self, other):
        if self.code == other.code:
            self.amount -= other.amount
        return self

    def __le__(self, other):
               if self.code == other.code:
                return self.amount <= other.amount
                return False

    def __ge__(self, other):
               if self.code == other.code:
                return self.amount >= other.amount
               return False

    def __int__(self):
              return int(self.amount)

    def __float__(self):
        """Convert to float"""
        return float(self.amount)


    def deposit(self, amount):
            self.amount += amount