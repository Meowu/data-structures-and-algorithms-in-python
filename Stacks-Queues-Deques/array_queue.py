from .array_stack import Empty


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues.

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # for gc
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, data):

        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + 1) % len(self._data)
        self._data[back] = data

    def _resize(self, cap):

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]  # place the old data from index 0.
            walk = (walk + 1) % len(old)  # ensure that we access the right index of old data
        self._front = 0  # reset the front after resizing.
