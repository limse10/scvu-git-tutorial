from operator import add, sub

#Question 1
def a_plus_abs_b(a, b):
    # """Return a+abs(b), but without calling abs.

    # >>> a_plus_abs_b(2, 3)
    # 5
    # >>> a_plus_abs_b(2, -3)
    # 5
    # """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# print(a_plus_abs_b(5,10))
# print(a_plus_abs_b(5,-10))

#Question 2
def two_of_three(a, b, c):
    # """Return x*x + y*y, where x and y are the two largest members of the
    # positive numbers a, b, and c.

    # >>> two_of_three(1, 2, 3)
    # 13
    # >>> two_of_three(5, 3, 1)
    # 34
    # >>> two_of_three(10, 2, 8)
    # 164
    # >>> two_of_three(5, 5, 5)
    # 50
    # """
    noList = [a,b,c]
    big1 = max(noList)
    noList.remove(max(noList))
    big2 = max(noList)

    return big1*big1 , big2*big2

#print(two_of_three(1,2,3))

#Question 3

def largest_factor(n):
    # """Return the largest factor of n that is smaller than n.

    # >>> largest_factor(15) # factors are 1, 3, 5
    # 5
    # >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    # 40
    # >>> largest_factor(13) # factor is 1 since 13 is prime
    # 1
    # """

    factor = []
    for i in range(1,n+1):
        if n%i==0:
            factor.append(i)

    if len(factor) == 2:
        print(f"Factor is 1 since {n} is a prime number")
    else:
        facs = ""
        for fac in factor:
            facs += " "+str(fac)
        print(f"Factors are{facs}")

#largest_factor(14)

#Question 4

def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

#Condition
def c():
    return False 

def t():
    print(1)
    return 1

def f():
    return 2

# print(with_if_function())
# print(with_if_statement())


#Question 5
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

# Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.

    "*** YOUR CODE HERE ***"
    print(n)
    i = 0
    while n != 1:
        if (n % 2) == 0:
            n = int(n/2)
            print(n)
        else:
            n = (n*3)+1
            print(n)
        i+=1
    print(f"Number of loops: {i}")

#hailstone(26)

