class Stack():
    def __init__(self):
        self.item = []

    def push(self, a):
        self.item.append(a)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def peek(self):
        if not self.item.is_empty():
            return self.item[-1]

    def get_item(self):
        return self.item()


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("d")
print(s.pop())

