#question 1
def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'has_seven',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    all_but_last, last = k//10, k % 10 #if number is 34347, it gets split up to be 3434.7
    if all_but_last > 1 or last ==7: #last == 7 accounts for the fact the number 7 has all_but_last 0 and if condition is not there it will go through else and return the result
                                    #as false
        if last  == 7:
            return True
        else:
            return has_seven(all_but_last)
    else:
        return False

print(has_seven(7))

#question2
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
#iteration method
    # l = []
    a = 0 #index just increases
    b = 0 #value increases and decreases, it depends
    direction = 1 #direction is "alive"
    #while a < n: #FOR A IN RANGE(N)
    while a < n:
        if (a!= 0 and a % 7 ==0) or has_seven(a): #a != 0 is to make sure 0 goes through else and increases
            direction = direction * -1
            b = b + direction
        else:
            b += direction
        a += 1
        #l.append(b)
    print(b)

pingpong(8) #rmb to call the function

#recursive method
def old_pingpong(n, a, b, direction): #create a new function to store the 4 variables
    #while a < n: #FOR A IN RANGE(N)
    if a < n:
        if (a!= 0 and a % 7 ==0) or has_seven(a):
            direction = direction * -1
            b = b + direction
            a += 1
            return old_pingpong(n, a, b, direction)
        else:
            b += direction
            a += 1
            return old_pingpong(n, a, b, direction)
        #l.append(b)
    return b

def pingpong(n):
    return old_pingpong(n, 1, 1, 1)

print(pingpong(8))
