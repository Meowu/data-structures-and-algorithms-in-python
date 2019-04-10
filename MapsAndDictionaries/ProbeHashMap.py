from MapsAndDictionaries.HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):

    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j
                if self._table[j] is None:
                    return False, first_avail
            elif k == self._table[j].key:
                return True, j
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s].value

    def _bucket_setitem(self, j, key, value):
        found, s = self._find_slot(j, key)
        if not found:
            self._table[s] = self._Item(key, value)
            self._n += 1
        else:
            self._table[s].value = value

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j].key
