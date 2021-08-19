""" Homework 1: Control """

# Q1
from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
       result= float(a+abs(b))
       return result
    else:
        result=float(a+b)
        return result



# Q2
def two_of_three(a, b, c):
    return x**2 + y**2 + z**2 - min(x, y, z) ** 2

def two_biggest(a, b, c):
    if a>=b>=c:
        return a**2+b**2
    elif b>=c>=a:
        return b**2+c**2
    else:
        return c**2 + a**2
# Q3
def largest_factor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
# Q4
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"

def t():
    "*** YOUR CODE HERE ***"

def f():
    "*** YOUR CODE HERE ***"

# Q5
    def hailstone(n):
        count = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = ((n * 3) + 1)
            print(n)
            count += 1
        print(count)



# Q6
quine = """
"*** YOUR CODE HERE ***"
"""