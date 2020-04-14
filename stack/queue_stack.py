from stack import Stack
class Queue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)
    
    def dequeue(self):
        if not self.stack_1.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())
            res = self.stack_2.pop()
            while not self.stack_2.is_empty():
                self.stack_1.push(self.stack_2.pop())
        return res

if __name__=='__main__':
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    print(q.dequeue())

        
    
    
