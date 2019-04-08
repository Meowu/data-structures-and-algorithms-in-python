from collections import MutableMapping


class MapBase(MutableMapping):
    __slots__ = '_key', '_value'

    class _Item(object):
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

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not(self < other)


class UnsortedTableMap(MapBase):

    _table: list[MapBase._Item]

    def __init__(self):
        self._table = []

    @property
    def table(self):
        return self._table

    def __len__(self):
        return len(self.table)

    def __setitem__(self, key, value):
        for item in self.table:
            if item.key == key:
                item.value = value
                return
        self.table.append(self._Item(key, value))

    def __getitem__(self, key):
        for item in self.table:
            if item.key == key:
                return item.value
        raise KeyError('Key Error: ' + repr(key))

    def __delitem__(self, key):
        for i in range(len(self)):
            if self.table[i].key == key:
                self.table.pop(i)
                return
        raise KeyError('Key Error: ' + repr(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

