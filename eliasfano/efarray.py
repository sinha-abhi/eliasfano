import math

class efarray():
    """
    A quasi-succinct representation of a non-decreasing sequence of 
    integers (in the mathematical sense).
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
        nel = len(sequence)
        lb = int(math.floor(math.log(bound / nel)))
        ulen = nel + (bound >> self.lb)

        self.lower = [None] * nel
        self.upper = [None] * ulen

        # TODO: populate the lower and upper bits arrays 

        # push `sequence` out of scope to free its memory
        del sequence 

    def __len__(self):
        # TODO: called for `len()`
        pass

    def __length_hint__(self):
        # TODO: not actually required, but just an optimization
        pass

    def __getitem__(self, key):
        # TODO: called for evaluation of self[key]
        pass

    def __setitem__(self, key, value):
        # TODO: this array should be immutable
        pass

    def __delitem__(self, key):
        # TODO: this array should be immutable
        pass

    def __contains__(self, item):
        # TODO: membership test operators
        pass

    def __iter__(self):
        # TODO: returns a new iterator over this container
        pass

    # Concatentation may require reconstructing the entire list in some cases.
    def __add__(self, other):
        # TODO: self + other
        pass

    def __iadd__(self, other):
        # TODO: other + self
        pass

    def __radd__(self, other):
        # TODO: self += other
        pass

    # Repetition can be implemented, but I don't see a use case
    # since the list will be immutable anyway.
    def __mul__(self, other):
        # TODO
        pass

    def __rmul__(self, other):
        # TODO
        pass

    def __imul__(self, other):
        # TODO
        pass

