class Buffer:
    def __init__(self):
        self.items = []
        self.pos = 0
        self.sum = 0
    def add(self, *a):
        for v in a:
            self.items.append(v)
            self.sum += v
            self.pos += 1
            if self.pos % 5 == 0:
                print(self.sum)
                self.sum = 0
    def get_current_part(self):
        res = self.items[self.pos-(self.pos % 5):self.pos]
        return res