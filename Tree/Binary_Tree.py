from .Tree import Tree


class BinaryTree(Tree):

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass ')

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass ')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if self.right(parent) == p:
            return self.left(parent)
        else:
            return self.right(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
