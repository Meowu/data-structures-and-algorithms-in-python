from .Tree import Tree


class BinaryTree(Tree):
    """
        A binary tree is an ordered tree with the following properties:
        1. Every node has at most two children.
        2. Each child node is labeled as being either a left child or a right child.
        3. A left child precedes a right child in the order of children of a node.
        
        A binary tree is proper if `each node` has either zero or two children.一个决策树 (decision tree) 也是完全二叉树，又叫满二叉树。

        二叉树有一些非常有意思的特性：
        1. We denote the set of all nodes of a tree T at the same depth d as level d of T .
        2. In general, level d has at most 2d nodes.

        对于一个非空完全二叉树，它有 Ne 个外部节点，Ni 个内部节点，那么可知 Ne = Ni + 1。
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
        if self.left(p) is not None:  # 遍历的时候从左到右。
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
