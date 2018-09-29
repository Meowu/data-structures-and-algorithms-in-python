
class Range:
    """A class that mimic's the build-in range class"""

    def __iter__(self, start, stop=None, step=1):
        """Initialize a Range instance
         Semantics is similar to build-in range class.
        """

        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        """Return the number of entries in the range."""
        return self._length

    def __getitem__(self, index):
        """Return entry at index item"""
        if index < 0:
            index += len(self)

        if not 0 <= index < self._length:
            raise IndexError('index out of range')

        return self._start + index * self._step
