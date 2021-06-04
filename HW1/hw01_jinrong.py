#01 A Plus Abs B
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# print(a_plus_abs_b(2, 3))
# print(a_plus_abs_b(2, -3))

#02 Two Of Three
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    x = max(a, b, c)
    y = add(add(a, b), c) - x - min(a, b, c)
    return x*x + y*y

# print(two_of_three(1, 2, 3))
# print(two_of_three(5, 5, 5))

#03 Largest Factor
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    b = 1
    while b < n:
        if n % b == 0:
            keep = b
            b += 1
        else:
            b += 1
            continue

    return keep

# print(largest_factor(15))
# print(largest_factor(80))

# 05: Hailstonn
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    i = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(int(n))
        else:
            n = n * 3 + 1
            print(int(n))
        i += 1
    return i

a = hailstone(10)
print(a)