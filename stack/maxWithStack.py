class MaxStack:
    def __init__(self):
        self.item = []

    def push(self, n):
        self.item.append(n)

    def is_empty(self):
        return self.item == []

    def pop(self):
        if not is_empty(self.item):
            self.item.pop()

    def peek(self):
        if not is_empty(self.item):
            return self.item[-1]

    def max(self):
        return max(self.item)

    def get_item(self):
        if not is_empty(self.item):
            return self.item()

if __name__=='__main__':
    ms = MaxStack()
    ms.push(1)
    ms.push(2)
    ms.push(3)
    print(ms.max())
    ms.push(7)
    print(ms.max())
    
    
