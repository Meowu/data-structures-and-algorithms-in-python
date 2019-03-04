from .Tree import Tree


class BinaryTree(Tree):
    """
        A binary tree is an ordered tree with the following properties:
        1. Every node has at most two children.
        2. Each child node is labeled as being either a left child or a right child.
        3. A left child precedes a right child in the order of children of a node.
        
        A binary tree is proper if `each node` has either zero or two children. 也就是
    """

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
        if self.left(p) is not None: # 遍历的时候从左到右。
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
