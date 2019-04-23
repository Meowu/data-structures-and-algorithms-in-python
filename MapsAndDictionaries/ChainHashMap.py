from MapsAndDictionaries.HashMapBase import HashMapBase
from MapsAndDictionaries.UnsortedMap import UnsortedTableMap


class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, key, value):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        old_size = len(self._table[j])
        self._table[j][key] = value
        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
