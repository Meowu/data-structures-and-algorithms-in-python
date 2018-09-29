class SequenceIterator:
    """
        An iterator for any of python's sequence types.
        任何定义了 __len__ 和 __getitem__ 方法的集合都可以被它迭代。
        This class can be instantiated as SequenceIterator(data)
    """

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._index = -1

    def __next__(self):
        """return the next element, else raise StopIteration error if index out of range"""

        self._index += 1
        if self._index < len(self._seq):
            return self._seq[self._index]
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""

        return self
