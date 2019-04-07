from Linked_List.DoublyLinkedList import Empty
from Priority_Queue.PriorityQueueBase import PriorityQueueBase


class HeapPriority(PriorityQueueBase):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self.data)

    @property
    def data(self):
        return self._data

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self)

    def _has_right(self, j):
        return self._right(j) < len(self)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _up_heap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[parent] > self.data[j]:
            self._swap(j, parent)
            self._up_heap(parent)

    def _down_heap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small = left
            if self._has_right(j):
                right = self._right(j)
                if self.data[self._right(j)] < self.data[left]:  # why select the smaller side?
                    small = right
            if self.data[small] < self.data[j]:  # need to compare the parent with child.
                self._swap(j, small)
                self._down_heap(small)

    def add(self, k, v):
        item = self._Item(k, v)
        self.data.append(item)
        self._up_heap(len(self) - 1)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self.data[0]
        return item.key, item.value

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self) - 1)
        item = self.data.pop()
        self._down_heap(0)
        return item.key, item.value


if __name__ == '__main__':
    h_queue = HeapPriority()
    assert h_queue.is_empty() is True, 'Initialize a empty queue.'
    h_queue.add(2, 'Two')
    h_queue.add(3, 'Three')
    assert len(h_queue) == 2, 'now h_queue has two item.'
    assert h_queue.min()[1] == 'Two', 'the first item with value `Two`'
    h_queue.add(1, 'One')
    assert h_queue.min()[0] == 1, 'now the first item with key 1'
    print('Tests ok.')
