#!/usr/env/bin python3

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """A version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of  Sequence."""

    @abstractmethod
    def __getitem__(self, i):
        """Return the element at index i of Sequence."""

    def __contains__(self, val):
        """Return True if val in Sequence else return False."""
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found or raise ValueError."""
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError("val is not in sequence."""

    def count(self, val):
        """Return the number of val in sequence."""
        count = 0
        for i in range(len(self)):
            if self[i] == val:
                count += 1
        return count
