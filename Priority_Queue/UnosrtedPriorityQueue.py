from .PriorityQueueBase import PriorityQueueBase
from Linked_List.PositionalList import PositionalList
from Linked_List.DoublyLinkedList import Empty


class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    @property
    def data(self):
        return self._data

    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        small = self.data.first()
        walk = self.data.after(small)
        while walk is not None:
            if walk.element < small.element:
                small = walk
            walk = self.data.after(walk)
        return small

    def __len__(self):
        return len(self.data)

    def min(self):
        p = self._find_min()
        item = p.element
        return item.key, item.value

    def remove_min(self):
        p = self._find_min()
        item = self.data.delete(p)
        return item.key, item.value

    def add(self, key, value):
        return self.data.add_last(self._Item(key, value))

