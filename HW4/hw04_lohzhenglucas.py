HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

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
    #from var outwards:
        #street obtains street value from a and b, then place into list via []
        #sorted sorts a and b in ascending order
        #item 1 is subtracted from item 0 in list (higher-lower) via -
        #repeat for avenue then add via +
    return (sorted([street(a), street(b)])[1]) - (sorted([street(a), street(b)])[0]) + (sorted([avenue(a), avenue(b)])[1]) - (sorted([avenue(a), avenue(b)])[0])
    

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"

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
    
    if n <= 3:
        return n
    if n > 3:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

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
    if n <= 3:
        return n
    else:
        #gn values used to store g(n-1), g(n-2) and g(n-3) respectively
        #they are set to g(1), (2) and (3) intially
        gn1 , gn2 , gn3 = 3 , 2 , 1
        #k is the current index of n 
        k = 4
        while k <= n:
            if sorted([gn1,gn2,gn3])[2] == gn1:
                gn3 = gn1 + 2*gn2 + 3*gn3
            elif sorted([gn1,gn2,gn3])[2] == gn3:
                gn2 = gn3 + 2*gn1 + 3*gn2 
            elif sorted([gn1,gn2,gn3])[2] == gn2:
                gn1 = gn2 + 2*gn3 + 3*gn1
            k = k+1
        #result must be the highest of gn values since derived by addition
        return sorted([gn1,gn2,gn3])[-1]

def coin_sizes_generator(amount):
    #1.1: iterative solution to generate all possible coin sizes for finite amount
    #1.2: declare and set intial values for vars
    #1.3: k is the power (increases each iteration)
    coin_size = 0
    k = -1 
    coinsizels = []
    while amount > coin_size:
        #since amount is finite, possible coin_sizes is finite too 
        k += 1
        coin_size = 2 ** k
        if amount >= coin_size: 
            coinsizels.append(coin_size)
        else:
            return coinsizels
    return coinsizels

def count_change(amount): 
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    #1: generate an list with all possible coin sizes (number_to_test) to test based on
    #2: does not change from start to finish of entire tree recursion
    csls = tuple(coin_sizes_generator(amount))
    #3: index of the first target testing number (+1 since using len)
    number_to_test = len(csls)
    #4: give recur csls (does not change), index of target testing number in csls, and amount (n)
    return recur(amount, csls, number_to_test)

def recur(n, csls, number_to_test):
    #5: BASE CASES
    if n == 0:
        #when amount is 0, there is 1 way to partition: no parts
        return 1
    elif n < 0:
        #when amount is less than 0, n cannot be subtracted by the coin value
        #hence return 0 since not a possibility
        return 0
    elif number_to_test <= 0 and n >= 1:
        #when the number_to_test is 0, index_to_test is -1
        #ie the list is empty
        #no way to partition with no parts.
        return 0
    #6: RECURSION TREE
    index_to_test = number_to_test - 1
    left_branch = recur(n - csls[index_to_test], csls, number_to_test)
        # for left branch, test the biggest coin by subtracting csls[index_to_test]
        # csls remains unchanged to keep index constant no matter the recursions
        # number_to_test remains same since need to test if csls[index_to_test] can be subtracted from n again
            # eg 8: 8-4=4, then do 4-4=0
    right_branch = recur(n, csls, number_to_test-1)
        #for right_branch, since the biggest coin has been tested on n, test the next biggest coin as the start of a new parent branch
        #hence n remains same but the number_to_test - 1 to refer to next index
        #when recurred, the number_to_test - 1 becomes index_to_test -1 due to line 50
        #csls remains unchanged as tuple.
    return right_branch + left_branch
        #result is sum of right and left branch

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
