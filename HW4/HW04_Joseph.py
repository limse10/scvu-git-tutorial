# Question 1
def intersection(st, ave):
    return (st+ave)*(st+ave+1)//2 + ave


def street(inter):
    return w(inter) - avenue(inter)


def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)


def taxicab(a, b):
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))


# Question 1 Test
print("Question 1 Test")
times_square = intersection(46, 7)
ess_a_bagel = intersection(51, 3)
print(taxicab(times_square, ess_a_bagel))
print(9)
print(" ")
print(taxicab(ess_a_bagel, times_square))
print(9)
print(" ")
# Question 3
"""
G(n) = n,                                       if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
"""
# recursive function
def g(n):
    if n <= 3:
        return n
    if n > 3:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


# g(n) Test
print("g(n) Test")
print(g(1))
print(1)
print(" ")
print(g(2))
print(2)
print(" ")
print(g(3))
print(3)
print(" ")
print(g(4))
print(10)
print(" ")
print(g(5))
print(22)
print(" ")

# iterative function
def g_iter(n):
    base = 3
    number1 = 1
    number2 = 2
    number3 = 3
    if n <= 3:
        return n 
    else:
        while base < n:
            new_number3 = number3 + (number2 * 2) + (number1 * 3)
            number1 = number2
            number2 = number3
            number3 = new_number3
            base += 1
    return number3

# g_iter(n) Test
print("g_iter(n) Test")
print(g_iter(1))
print(1)
print(" ")
print(g_iter(2))
print(2)
print(" ")
print(g_iter(3))
print(3)
print(" ")
print(g_iter(4))
print(10)
print(" ")
print(g_iter(5))
print(22)
print(" ")

# Question 4
def count_change(amount):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    # largest coin that can be used to make change
    def largest_coin(x):
        if x <= 0:
            return 0
        else:
            a = 1
            while a < x:
                a = a * 2
        return a
    # count the ways to make change for that amount
    def cchelper(n, m):
            
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        elif m == 1:
            return 1
        else:
            return cchelper(n - m, m) + cchelper(n, m // 2)
    return cchelper(amount, largest_coin(amount))

# Question 4 Test
print("Question 4 Test")
print(count_change(7))
print(6)
print(count_change(10))
print(14)
print(count_change(20))
print(60)
print(count_change(100))
print(9828)
