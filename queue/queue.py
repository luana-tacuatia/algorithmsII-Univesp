# Implement a program to manage two types of queues in a bank:
    # 1 - preferential line for elders (>=60 years)
    # 2 - common line for those with less than 60 years
# Also, when people are 'called by the clerk', remove them of the line in the following proportion: 2:1 (>=60:<60)

class Queue():
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0

    def __len__(self):
        return len(self.data)


priority_line = Queue()
common_line = Queue()

age = input("Hello. How old are you?")

while age.isnumeric():
    numeric_age = int(age)
    if numeric_age >= 60:
        priority_line.insert(age)
    else:
        common_line.insert(age)
    age = input("Hello. How old are you?")

while not priority_line.empty() or not common_line.empty():
    if priority_line.__len__() >= 2 and not common_line.empty():
        print(priority_line.remove())
        print(priority_line.remove())
        print(common_line.remove())
    elif priority_line.__len__() == 1 and not common_line.empty():
        print(priority_line.remove())
        print(common_line.remove())
    elif priority_line.__len__() == 0 and not common_line.empty():
        print(common_line.remove())
    else:
        print(priority_line.remove())



