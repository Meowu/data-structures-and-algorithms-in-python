from MapsAndDictionaries.HashMapBase import MapBase


class SortedTableMap(MapBase):

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self.table[mid]._key:
                return mid
            elif k < self.table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __init__(self):
        self._table = []

    @property
    def table(self):
        return self._table

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self.table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j].value

    def __setitem__(self, key, value):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == key:
            self._table[j]._value = value
        else:
            self._table.insert(j, self._Item(key, value))

    def __delitem__(self, key):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != key:
            raise KeyError('Key Error: ' + repr(key))
        self._table.pop(j)

    def __iter__(self):
        for item in self.table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return self._table[0]._key, self.table[0]._value
        else:
            return None

    def find_max(self):
        if len(self.table) > 0:
            return self.table[-1]._key, self.table[-1]._value
        else:
            return None

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table):
            return self.table[j]._key, self.table[j].value
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j > 0:
            return self.table[j]._key, self._table[j-1]._value
        else:
            return None

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table[j]._key == k:
            j += 1
        if j < len(self.table):
            return self.table[j]._key, self.table[j]._value
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
            while j < len(self.table) and (stop is None or self.table[j]._key < stop):
                yield self.table[j]._key, self.table[j]._value
                j += 1


