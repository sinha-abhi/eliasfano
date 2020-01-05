import collections.Sequence
import math

# TODO: A lot of the comments can be removed in the future. I only put them
# there to make sure my reasoning is sound.
class efarray():
    """
    An immutable quasi-succinct representation of a non-decreasing sequence of 
    integers. See Elias-Fano encoding for more details.
    """

    def __init__(self, sequence, issorted=False):
        """
        Initialize an Elias-Fano encoded sorted sequence.

        Parameters
        ----------
        sequence : array_like
            List of integers, preferably sorted.
        """
        # Best case (already sorted) is O(n), worst case O(n log n).
        # Checking if sorted is O(n), so we gain nothing by checking.
        sequence = sorted(sequence)

        self.offset = 0
        if sequence[0] < 0:
            # The first element is always 0.
            # In the future, we can possiby save negligable memory 
            # by not storing the 0. Likely not worth it.
            self.offset = abs(sequence[0])
            sequence = [x + self.offset for x in sequence]

        bound = sequence[-1] + 1
        self.nel = len(sequence)
        lb = int(math.floor(math.log(bound / self.nel)))
        ulen = self.nel + (bound >> self.lb)

        self.lower = [None] * self.nel
        self.upper = [None] * ulen

        # TODO: populate the lower and upper bits arrays 

        # push `sequence` out of scope to free its memory
        del sequence 

    def __len__(self):
        # TODO: called for `len()`
        return self.nel

    def __length_hint__(self):
        # TODO: not actually required, but just an optimization
        raise NotImplementedError

    def __getitem__(self, index):
        if index < 0 or index >= self.nel:
            raise IndexError
        else:
            # TODO: called for evaluation of self[index]
            #       Can we possibly do this in constant time?
            raise NotImplementedError

    def __setitem__(self, index, value): pass

    def __delitem__(self, key): pass

    def __contains__(self, value):
        # This will have the same problem as `__iter__`. See below.
        for v in self:
            if v is value or v == value:
                return True
        return False

    def __iter__(self):
        # If `__getitem__` is not implemented in such a way that elements are
        # accessed in constant time, then this method of generating an iterable
        # may be painfully slow. I can't see any way around it.
        try:
            i = 0
            while True:
                v = self[i]
                yield v
                i += 1
        except IndexError:
            return

    # Concatentation may require reconstructing the entire list in some cases.
    def __add__(self, other):
        # TODO: self + other
        raise NotImplementedError

    def __iadd__(self, other):
        # TODO: other + self
        raise NotImplementedError

    def __radd__(self, other):
        # TODO: self += other
        raise NotImplementedError

    # Repetition can be implemented, but I don't see a use case
    # since the list will be immutable anyway.
    def __mul__(self, other):
        # TODO
        raise NotImplementedError

    def __rmul__(self, other):
        # TODO
        raise NotImplementedError

    def __imul__(self, other):
        # TODO
        raise NotImplementedError

Sequence.register(efarray)
