# -*- coding: utf-8 -*-
from ..Linked_List.LinkedQueue import LinkedQueue


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

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def bread_first(self):
        if not self.is_empty():
            queue = LinkedQueue()
            queue.enqueue(self.root())
            while not queue.is_empty():
                p = queue.dequeue()
                yield p
                for c in p.children(p):
                    queue.enqueue(c)

    def positions(self):
        """
        Generate an iteration of all positions of tree T.
        :return: 
        """
        # raise NotImplementedError('must be implemented by subclass ')
        return self.pre_order()

    def _subtree_pre_order(self, p):
        yield p
        for child in self.children(p):
            for other in self._subtree_pre_order(child):
                yield other

    def pre_order(self):
        if not self.is_empty():
            for p in self._subtree_pre_order(self.root()):
                yield p

    def _subtree_post_order(self, p):
        for c in p.children():
            for n in self._subtree_post_order(c):
                yield n
        yield p

    def post_order(self):
        if not self.is_empty():
            for p in self._subtree_post_order(self.root()):
                yield p

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
        This implementation is more efficient than self._height1.O(n)
        :return: 
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """
        # 一个通用的计算任意节点的高度。
        :param p: 
        :return: 
        """
        if p is None:
            p = self.root()
        return self._height2(p)


if __name__ == "__main__":
    t = Tree()
    print('called.')
    t.root()
