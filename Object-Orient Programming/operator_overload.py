class Vector:
    """ Represent a Vector in a multidimensional space."""

    def __init__(self, d):
        """Create a multidimensional vector of zeros."""
        self._coords = [0] * d

    def get_coordinates(self):
        """return current coordinates"""
        return self._coords

    def __len__(self):
        """return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, i):
        """return the ith coordinate of vector"""
        return self._coords[i]

    def __setitem__(self, i, val):
        """set the ith coordinate of vector."""
        self._coords[i] = val

    def __add__(self, other):
        """sum the two vector and return the result."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree.')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        """return True if vector has the same coordinates as other"""
        return self._coords == other.get_coordinates()

    def __ne__(self, other):
        """return True if vector differs from other"""
        return not self == other  # rely on __eq__ method.

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1, -1] + '>'
