from Priority_Queue.HeapPriorityQueue import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):

    class Locator(HeapPriorityQueue._Item):

        def __init__(self, k, v, i):
            super().__init__(k, v)
            self._index = i

        @property
        def index(self):
            return self._index

        @index.setter
        def index(self, i):
            self._index = i

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i].index = i
        self._data[j].index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._up_heap(j)
        else:
            self._down_heap(j)

    def add(self, k, v):
        token = self.Locator(k, v, len(self))
        self._data.append(token)
        self._up_heap(len(self) - 1)
        return token

    def update(self, loc: Locator, new_val: any, new_key: int):
        index = loc.index
        if not (0 <= index < len(self) and self._data[index] is loc):
            raise ValueError('invalid locator.')
        loc.value = new_val
        loc.key = new_key
        self._bubble(index)

    def remove(self, loc: Locator):
        index = loc.index
        if not (0 <= index < len(self) and self._data[index] is loc):
            raise ValueError('invalid locator.')
        if index == len(self) - 1:
            self._data.pop()
        else:
            self._swap(index, len(self) - 1)
            self._data.pop()
            self._bubble(index)
        return loc.key, loc.value
