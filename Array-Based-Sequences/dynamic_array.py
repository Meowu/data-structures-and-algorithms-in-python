import ctypes


class DynamicArray:
    def __init__(self):

        self._n = 0
        self._capacity = 1
        self._A = _make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):

        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):

        if self._n == self._capacity:
            return self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in (self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        # remove 方法总是需要 O(n) 因为遍历后需要把后面往前移。
        for i in range(self._n):
            if self._A[i] == value:
                for k in range(i, self._n - 1):
                    self._A[k] = self._A[k + 1]
                self._A[self._n - 1] = None  # for garbage collection.
            return

        raise ValueError('value not found.')


def _resize(self, c):
    B = self._make_array(c)
    for i in range(self._n):
        B[i] = self._A[i]
    self._A = B
    self._capacity = c


def _make_array(self, c):
    return (c * ctypes.py_object)()