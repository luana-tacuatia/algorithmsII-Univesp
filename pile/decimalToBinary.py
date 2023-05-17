# Implement a method to convert a decimal number into a binary one using pile.

class Pile():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        return not len(self.data) > 0

p = Pile()
num = int(input("Type a decimal number to be converted into a binary one."))

while num > 0:
    p.push(num % 2)
    num = num // 2

while not p.empty():
    print(p.pop())



