from .PriorityQueueBase import PriorityQueueBase
from Linked_List.PositionalList import PositionalList
from Linked_List.DoublyLinkedList import Empty


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    @property
    def data(self):
        return self._data

    def __len__(self):
        return len(self.data)

    def add(self, key, value):
        new = self._Item(key, value)
        walk = self.data.last()
        while walk is not None and walk.element > new:
            walk = self.data.before(walk)
        if walk is None:
            self.data.add_first(new)
        else:
            self.data.add_after(walk, new)

    def min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty.')
        p = self._data.first().element
        return p.key, p.value

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty.')
        item = self.data.delete(self.data.first())
        return item.key, item.value
