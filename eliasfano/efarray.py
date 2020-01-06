import collections.Sequence
import math

# TODO: A lot of the comments can be removed in the future. I only put them
# there to explain my reasoning is sound. The main point of this library is to
# be memory efficient (I would save performance is equally important, but there
# is no way we can match the performance of the generic list). 
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
        issorted : boolean
            Passing `True` is equivalent to providing a guarentee that the
            provided sequence is indeed sorted; i.e. no checks shall be made
            internally to ensure that fact. If the sequence is not sorted, 
            then the behavior of this class is undefined.
        """
        # Best case (already sorted) is O(n), worst case O(n log n).
        # Checking if sorted is O(n), so we gain nothing by checking.
        if not issorted:
            sequence = sorted(sequence)
        elif __debug__:
            print("Warning: no check for sorted sequence")

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

        # Actually, I don't think we want to use a `list` here because of space
        # issues. I haven't tried to find the point at which using a list
        # becomes more efficient than using an int (if there is one at all).
        # Python has arbitrarily long ints now anyway.
        #
        # I did find using ints will save much more space. Here is some quick
        # test code (based on the example in the notes pdf):
        """
        print("using int")
        a = 0b10100001100
        print(bin(a))
        print(sys.getsizeof(a))

        print("using list")
        b = [0b01, 0b00, 0b00, 0b11, 0b00]
        print(b)
        print(sys.getsizeof(b))
        """
        # This gives the following:
        """
        using int
        0b10100001100
        28
        using list
        [1, 0, 0, 3, 0]
        112
        """
        # So, I think a good way to to do it would be to have the lower bits
        # array be initialized like:
        #       self.lower = 1 << self.nel
        # and then ignore the first bit of the array. Something similar will
        # hold for the upper bits array.
        self.lower = [None] * self.nel
        self.upper = [0] * ulen

        # TODO: populate the lower and upper bits arrays 

        # push `sequence` out of scope to free its memory
        del sequence 

    def __split__(self, index, value):
        # Not sure if these needs to be its own method. I'm thinking that we
        # may eventually have an optional parallel way of processing the 
        # elements of the sequence, but I'd have to check if that actually 
        # gives us any performance benefit before hand. If we decide not to 
        # do that, then this probably doesn't need to be its own method.
        """
        Extract the lower and upper bits for the given value in the context of
        the current efarray.
        
        Parameters
        ----------
        value : integer type
            Value in the sequence.

        Returns
        -------
        upper : integer type
            Bits to be put in upper-bit array.
        lower : integer type
            Bits to be put in lower-bits array.
        """
        upper, lower = -1, -1

        # TODO: implement splitting

        return upper, lower

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
