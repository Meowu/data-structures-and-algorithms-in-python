class ListTree(object):

    def __init__(self, root, left=[], right=[]):
        self._tree = [root, left, right]

    def tree(self):
        return self._tree

    def insert_left(self, item):
        t = self.tree().pop(1)
        if len(t) > 0:
            self.tree().insert(1, [item, t, []])
        else:
            self.tree().insert(1, [item, [], []])

    def insert_right(self, item):
        t = self.tree().pop(2)
        if len(t) > 0:
            self.tree().insert(2, [item, [], t])
        else:
            self.tree().insert(2, [item, [], []])

    def root(self):
        return self.tree()[0]

    def get_left(self, t):
        return t[1]

    def get_right(self, t):
        return t[2]

    def set_root(self, t):
        self.tree()[0] = t
