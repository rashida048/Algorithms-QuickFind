class QuickUnion(object):
    def __init__(self, N):
      self.lst = list(range(N))

    def get_root(self, ind):
      while ind != self.lst[ind]:
          ind = self.lst[ind]
      return ind

    def find(self, a, b):
      return self.get_root(a) == self.get_root(b)

    def union(self, a, b):
      root_a = self.get_root(a)
      self.lst[root_a] = self.get_root(b)


first = QuickUnion(8)

print(first.union(1,5))
print(first.lst)
