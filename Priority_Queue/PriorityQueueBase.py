

class PriorityQueueBase(object):

    class _Item(object):

        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0
