

class PriorityQueueBase(object):

    class _Item(object):

        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        @property
        def key(self):
            return self._key

        @key.setter
        def key(self, k):
            self._key = k

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, v):
            self._value = v

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0
