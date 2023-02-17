def factorial(n):
    """
    >>> factorial(3)
    6

    >>> factorial (5)
    120
    """
    if n == 1:
        return n
    return n * factorial(n-1)


def test_factorial():
    assert factorial(3) == 6


if __name__ == "__main__":
    import doctest
    doctest.testmod()
