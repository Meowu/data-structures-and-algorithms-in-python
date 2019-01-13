class Tree(object):

    class Position(object):

        def element(self):
            raise NotImplementedError('must be implemented by subclass ')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass ')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subclass ')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass ')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass ')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass ')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass ')

    def positions(self):
        raise NotImplementedError('must be implemented by subclass ')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_root(p))  # O(n^2) in worst-case time

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)
