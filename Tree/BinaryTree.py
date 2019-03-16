class BinaryTree(object):

    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None

    def insertLeft(self, val):
        if self.left is None:
            self.left = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.left = self.left
            self.left = t

    def insertRight(self, val):
        if self.right is None:
            self.right = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.right = self.right
            self.right = t

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getRoot(self):
        return self.root

    def setRoot(self, val):
        self.root = val


if __name__ == '__main__':
    t = BinaryTree('a')
    assert t.getRoot() == 'a', 'should be a'
    t.insertLeft('b')
    assert 'b' == t.getLeft().getRoot(), 'should be b'
    t.insertRight('c')
    assert 'c' == t.getRight().getRoot(), 'should be c'
    t.getLeft().setRoot('new left')
    assert 'new left' == t.getLeft().getRoot(), 'should be new left'
