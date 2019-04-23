from .Binary_Tree import BinaryTree


class LinkedBinaryTree(BinaryTree):

    class Node(object):

        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        @property
        def element(self):
            return self._element

        @element.setter
        def element(self, el):
            self._element = el

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, p):
            self._parent = p

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, p):
            self._left = p

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, p):
            self._right = p

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        @property
        def node(self):
            return self._node

        @node.setter
        def node(self, n):
            self._node = n

        @property
        def container(self):
            return self._container

        @container.setter
        def container(self, c):
            self._container = c

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper type.')
        if p.container is not self:
            raise ValueError('p does not belong to this tree.')
        if p.node.parent is p.node:
            raise ValueError('deprecated node.')
        return p.node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    # @property
    # def root(self):
    #     return self._root
    #
    # @root.setter
    # def root(self, r):
    #     self._root = r

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.right is not None:
            count += 1
        if node.left is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('root exists.')
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError('right exists')
        self._size += 1
        node.right = self.Node(e, node)
        return self._make_position(node.right)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('left exist.')
        self._size += 1
        node.left = self.Node(e, node)
        return self._make_position(node.left)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node.element
        node.element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children.')
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        node.parent = node
        return node.element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('p must be a leaf.')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must be the same.')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node.left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root_parent = node
            node.right = t2._root
            t2._root = None
            t2._size = 0
