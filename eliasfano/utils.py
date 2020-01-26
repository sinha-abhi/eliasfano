"""
Bit manipulation methods.
"""

def extract(word, pos, k):
    """
    Extracts k bits starting from pos of a word.
    
    Note that if the k bits are not padded with 0s.
    Suppose the k bits are 00, then this method will return 0b0.
    Suppose the k bits are 01, then this method will return 0b1.
    """
    return (((1 << k) - 1) & (word >> pos))


def ffs(word):
    """
    Finds the position of the least significant bit set to one in a word.
    """
    return (word & (-word)).bit_length() - 1


def lower(word, k):
    """
    Returns the least significant k bits in a word.
    """
    return word & ((1 << k) - 1)


def replace(word, pos, k, val):
    """
    Replace k bits starting from pos of a word with val.
    """
    mask = (((1 << (pos + k)) - 1) >> pos) << pos
    return (word & ~mask) | ((val << pos) & mask)
    

def setbit(word, k):
    """
    Sets the kth bit of a word; i.e. flips that bit to 1.
    """
    return ((1 << k) |  word)

