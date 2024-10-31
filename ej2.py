import doctest

def sum(a,b):
    """
    >>> sum(1,2)
    3
    """
    return a + b
print(sum(1,2))
doctest.testmod()