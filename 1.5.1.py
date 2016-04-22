class MoneyBox:
    amount=0

    def __init__(self, capacity=0):
        self.capacity = capacity

    def can_add(self, v):
        if (self.amount + v) <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.amount += v
