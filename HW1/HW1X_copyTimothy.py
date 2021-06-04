#question1
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

print(a_plus_abs_b(2,3))

#question2
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
    y = add(add(a,b), c) - x - min(a,b,c) #to find the 2nd biggest number
    return x*x + y*y
print(two_of_three(5,5,5))

#question3
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
    b = 1 #all numbers have 1 as their factor so it is similar to the "Base Case"
    while b < n:
        if n % b == 0 and b !=0: #factors cannot be 0 and b must be divisible by n 
            keep = b #we store the values of b in "keep"
            b += 1
        else:
            b += 1
            continue
    return keep

print(largest_factor(80))

#question 4
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
    print(int(n)) #for the first hailstone,n to appear on the doctest
    i = 1 #to be a counter
    while n != 1:
        if n % 2 == 0:
            n = n/2 
            print(int(n))
        else:
            n = (n*3) + 1
            print(int(n))
        i += 1
    return i

a = hailstone(10)
print(a)

