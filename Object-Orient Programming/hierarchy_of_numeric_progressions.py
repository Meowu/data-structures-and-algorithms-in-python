#!/usr/env/bin python3


class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance() # advance to prepare for next time
            return answer
    
    def __iter__(self):
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))

    def print_current(self):
        """Print the current"""
        print(self._current)


class ArithmeticProgression(Progression):

    def __init__(self, step=1, start=0):
        super().__init__(start)
        self._step = step

    def _advance(self):
        self._current += self._step


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == "__main__":
    print("exec progression: ")
    pg = Progression()
    print("first value: {0}".format(next(pg)))
    print("next 9 value")
    pg.print_progression(9)
    pg.print_current()
    fp = FibonacciProgression(0, 1)
    print(str(next(fp)))
