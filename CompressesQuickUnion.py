class CompressedQuickUnion(object):
    def __init__(self, N):
      self.lst = list(range(N))

    def get_root(self, ind):
      seen = set([])
      while ind != self.lst[ind]:
          # Point to the grandparent. This will always work as the
          # root points to itself.
          self.lst[ind] = self.lst[self.lst[ind]]
          ind = self.lst[ind]
      return ind

    def find(self, a, b):
      return self.get_root(a) == self.get_root(b)

    def union(self, a, b):
      root_a = self.get_root(a)
      self.lst[root_a] = self.get_root(b)

first = CompressedQuickUnion(10)

print(first.union(1,5))
print(first.lst)
