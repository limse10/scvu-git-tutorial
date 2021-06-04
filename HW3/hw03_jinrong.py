#01: Has Seven
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
    allbutlast, last = k // 10, k % 10
    if allbutlast > 1 or last == 7:
        if last == 7:
            return True
        else:
            return has_seven(allbutlast)
    else:
        return False

# print(has_seven(3))
# print(has_seven(2734))

#02: Ping-pong
def pingpong(n, a, b, direction):
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
    # l = []
    # a = 0 # index
    # b = 0 # value
    # direction = 1
    # while a < n:
    if a < n:
        if (a % 7 == 0 and a != 0) or has_seven(a):
            direction = direction * -1
            b = b + direction
        else:
            b += direction
        a += 1
        return pingpong(n, a, b, direction)
    return b


print(pingpong(8, 1, 1, 1))