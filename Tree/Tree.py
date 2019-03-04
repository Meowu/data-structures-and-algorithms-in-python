# -*- coding: utf-8 -*-

class Tree(object):
    """
    Tree ADT.
    所有接收 p 作为其参数的方法需要保证 p 是 Tree 的合法节点，不然应抛出异常。
    
    这里不定义任何创建或修改树的方法。这些方法应该基于不同的树的实现而不同。
    """

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
        """
        Generate an iteration of all positions of tree T.
        :return: 
        """
        raise NotImplementedError('must be implemented by subclass ')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """
        The depth of p is the number of ancestors of p, excluding p itself.
        Note that this definition implies that the depth of the root of T is 0. 
        :param p: 
        :return: 
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """
        The height of a nonempty tree T is equal to the maximum of
        the depths of its leaf positions.
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))  # O(n^2) in worst-case time

    def _height2(self, p):
        """
        If p is a leaf, then the height of p is 0, else the height of p is one more than 
        the maximum of the heights of p’s children.
        :return: 
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)


if __name__ == "__main__":
    t = Tree()
    print('called.')
    t.root()