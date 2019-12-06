class WeightedQuickUnion(object):
    def __init__(self, N):
      self.lst = list(range(N))
      self.sizes = [1] * N

    def get_root(self, ind):
      while ind != self.lst[ind]:
          ind = self.lst[ind]
      return ind

    def find(self, a, b):
      return self.get_root(a) == self.get_root(b)

    def union(self, a, b):
      if self.sizes[self.get_root(a)] < self.sizes[self.get_root(b)]:
          self.lst[self.get_root(a)] = self.get_root(b)
          self.sizes[self.get_root(b)] += self.sizes[self.get_root(a)]
      else:
          self.lst[self.get_root(b)] = self.get_root(a)
          self.sizes[self.get_root(a)] += self.sizes[self.get_root(b)]

first = WeightedQuickUnion(10)

print(first.union(4,3))
print(first.lst)


