class QuickFind(object):
    def __init__(self, N):
        self.lst = list(range(N))

    def find(self, a, b):
        return self.lst[a] == self.lst[b]
    
    def union(self, a, b):
        old = self.lst[a]
        new = self.lst[b]
        for ind, x in enumerate(self.lst):
            if x == old:
                self.lst[ind] = new

first = QuickFind(10)

print(first.union(3, 4))
print(first.lst)
print(first.union(3, 8))
print(first.lst)
