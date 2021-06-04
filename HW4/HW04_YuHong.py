#Question 1

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

interX = intersection(51,3)
interY = intersection(46,7)

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

# For example, Times Square is on 46th Street and 7th Avenue. Ess-a-Bagel is on 51st Street and 3rd Avenue. 
# The taxicab distance between them is 9 blocks (5 blocks from 46th to 51st street and 4 blocks from 7th avenue to 3rd avenue). 
# Taxicabs cannot cut diagonally through buildings to reach their destination!

#Implement taxicab, which computes the taxicab distance between two intersections using the following data abstraction. 
#Hint: You don't need to know what a Cantor pairing function is; just use the abstraction.

    stX = street(a)
    avX = avenue(a)
    stY = street(b)
    avY = avenue(b)

    dist = (abs(stX - stY) + abs(avX - avY))
    print(f"Distance between the two intersection is {dist} blocks")


#taxicab(interX,interY)


#Question 3

#A mathematical function G on positive integers is defined by two cases:
# G(n) = n,                                       if n <= 3
# G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
# g4 = g(4-1) + 2* g()
# g5 = g4(10) + 2x3 + 3x2
#       10      6       6

# Write a recursive function g that computes G(n). Then, write an iterative function g_iter that also computes G(n):
# Hint: The fibonacci example in the tree recursion lecture is a good illustration of the relationship between the recursive and iterative definitions of a tree recursive problem.

def g(n):
    # """Return the value of G(n), computed recursively.

    # >>> g(1)
    # 1
    # >>> g(2)
    # 2
    # >>> g(3)
    # 3
    # >>> g(4)
    # 10
    # >>> g(5)
    # 22
    # >>> from construct_check import check
    # >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    # True
    # """
    # "*** YOUR CODE HERE ***"

    if n > 3:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
    else: 
        return n

#print(g(6))


def g_iter(n):
    # """Return the value of G(n), computed iteratively.

    # >>> g_iter(1)
    # 1
    # >>> g_iter(2)
    # 2
    # >>> g_iter(3)
    # 3
    # >>> g_iter(4)
    # 10
    # >>> g_iter(5)
    # 22
    # >>> from construct_check import check
    # >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    # True
    # """
    # "*** YOUR CODE HERE ***"

    #4 >> g3 + 2xg2 + 3xg1
    #5 >> g4 + 2xg3 + 3xg2

    if n > 3:
        count = 3
        no1 = 3
        no2 = 2
        no3 = 1
        temp2 = 0
        temp3 = 0
        while count < n:
            #print(f"Front G{count}: {no1}")
            #print(f"no2: {no2}")
            #print(f"no3: {no3}")
            temp1 = no1
            temp2 = no2

            no1 = no1 + 2*no2 + 3*no3
            no2 = temp1
            no3 = temp2

            count += 1

        return no1

    else:
        return n

#print(g_iter(6))

#Question 4


# Once the machines take over, the denomination of every coin will be a power of two: 1-cent, 2-cent, 4-cent, 8-cent, 16-cent, etc. 
# There will be no limit to how much a coin can be worth.

# Given a positive integer amount, a set of coins makes change for amount if the sum of the values of the coins is amount. For example, the following sets make change for 7:
# 7 1-cent coins
# 5 1-cent, 1 2-cent coins
# 3 1-cent, 2 2-cent coins
# 3 1-cent, 1 4-cent coins
# 1 1-cent, 3 2-cent coins
# 1 1-cent, 1 2-cent, 1 4-cent coins

# Thus, there are 6 ways to make change for 7. Write a recursive function count_change that takes a positive integer amount and 
# returns the number of ways to make change for amount using these coins of the future.

# Hint: Refer the implementation of count_partitions for an example of how to count the ways to sum up to an amount with smaller parts. 
# If you need to keep track of more than one value across recursive calls, consider writing a helper function.

def count_change(amount):
    # """Return the number of ways to make change for amount.

    # >>> count_change(7)
    # 6
    # >>> count_change(10)
    # 14
    # >>> count_change(20)
    # 60
    # >>> count_change(100)
    # 9828
    # >>> from construct_check import check
    # >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    # True
    # """
    # "*** YOUR CODE HERE ***"
    def count_part(value,parts):

        if value == 0:
            #print("TEST1")
            return 1
        elif value < 0 or value < parts:
            #print("TEST2")
            return 0
        else:
            print(f"Parts now is: {parts}")
            with_part = count_part(value-parts,parts)
            without_part = count_part(value, parts*2)
            return with_part + without_part


    return count_part(amount,1)

print(count_change(7))
