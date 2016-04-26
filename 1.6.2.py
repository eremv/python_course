class ExtendedStack(list):
    def __init__(self):
        self=[]
    def sum(self):
        self.append(stack.pop()+stack.pop())
    def sub(self):
        self.append(stack.pop()-stack.pop())
    def mul(self):
        self.append(stack.pop()*stack.pop())
    def div(self):
        self.append(stack.pop()/stack.pop())
