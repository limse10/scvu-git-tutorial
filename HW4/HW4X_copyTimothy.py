def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    
    return abs((street(a))-street(b)) + abs(avenue(a) - avenue(b))

times_square = intersection(46, 7)
ess_a_bagel = intersection(51, 3)
print(taxicab(times_square, ess_a_bagel))
print(taxicab(ess_a_bagel, times_square))

#question 3

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
def g(n):
    if n <=3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)
print(g(5))


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n 
    else:
        i = 3
        x, y, z = 1, 2, 3
        # new = 0
        while i < n:
            # new = z + 2*y +3*x
            x, y, z = y, z, z + 2*y +3*x
            i += 1
        return z

# print(g_iter(5))

    if n <= 3:
        return n
    else:
        all = [1, 2, 3]
        i = 3
        m = 1
        while i < n:
            m = all[i-1] + (all[i-2] * 2) + (all[i-3] * 3)
            all.append(m)
            i += 1
        return m
    
def count_change(amount):
    """Return the number of ways to make change for amount."""
    "*** YOUR CODE HERE ***"

    def findm(amount):
        a = 1
        i = 0 
        while 2**i < amount:
            i += 1
            a = 2**(i-1)
        return a 

    def count_partitions(n, m):
        """Count the ways to partition n using parts up to m."""
        # print(n,m)
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return count_partitions(n-m, m) + count_partitions(n, m//2)

    c = findm(amount) #need to call the function 
# print(c)
    b = count_partitions(amount, c)
# print(b)
    return b

print(count_change(20))

#done hehe