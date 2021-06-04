#05: Counter
def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    "*** YOUR CODE HERE ***"
    dic = {}
    def d(n):
        # print(dic.get(n))
        if dic.get(n): #false
            dic[n] = dic.get(n) + 1
            return dic.get(n)
        else:
            dic[n] = 1
            return 1
            
    return d

# c = make_counter()
# print(c('a'))
# print(c('a'))
# print(c('b'))
# print(c('a'))
# c2 = make_counter()
# print(c2('b'))
# print(c2('b'))
# print(c('b') + c2('b'))

#06: Next Fibonacci
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    a = 0  #current 
    b = 1  #next
    def fib():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result
    return fib

# fib = make_fib()
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# fib2 = make_fib()
# print(fib() + sum([fib2() for _ in range(5)]))

#07: Password Protected Account
'''def make_withdraw(balance):
    """Return a withdraw function with BALANCE as its starting balance.
    >>> withdraw = make_withdraw(1000)
    >>> withdraw(100)
    900
    >>> withdraw(100)
    800
    >>> withdraw(900)
    'Insufficient funds'
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw'''

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    a_list = []
    def withdraw(amount, test_password):
        nonlocal balance, password
        if len(a_list) < 3:
            if test_password == password:
                if amount > balance:
                    return 'Insufficient funds'
                else:
                    balance = balance - amount
                    return balance
            else:
                a_list.append(test_password)
                # print(a_list)
                return 'Incorrect password'
        else:
            return 'Your account is locked. Attempts: {}'.format(a_list)
    return withdraw
    # def withdraw(amount):
    #     nonlocal balance
    #     if amount > balance:
    #        return 'Insufficient funds'
    #     balance = balance - amount
    #     return balance
    
    # def check_pasword(amount, test_password):
    #     if len(a_list) == 3:
    #         return 'Your account is locked. Attempts: {}'.format(a_list)
    #     else:
    #         if password == test_password:
    #             return withdraw(amount)
    #         else:
    #             a_list.append(test_password)
    #             return 'Incorrect password'
    # return check_pasword


# w = make_withdraw(100, 'hax0r')
# print(w(25, 'hax0r'))
# error = w(90, 'hax0r')
# print(error)
# error = w(25, 'hwat')
# print(error)
# new_bal = w(25, 'hax0r')
# print(new_bal)
# print(w(75, 'a'))
# print(w(10, 'hax0r'))
# print(w(20, 'n00b'))
# print(w(10, 'hax0r'))
# print(w(10, 'l33t'))

#08: Joint Account
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    a = withdraw(0, old_password)
    if type(a) == int:
        
        def test_new(amount, new_new_password):
            if new_new_password == new_password:
                return withdraw(amount, old_password)
            elif new_new_password == old_password:
                return withdraw(amount, old_password)
            else:
                return withdraw(amount, new_new_password)
        
        return test_new
    else:
        return a

w = make_withdraw(100, 'hax0r')
print(w(25, 'hax0r'))
print(make_joint(w, 'my', 'secret'))
j = make_joint(w, 'hax0r', 'secret')
print(w(25, 'secret'))
print(j(25, 'secret'))
print(j(25, 'hax0r'))
print(j(100, 'secret'))

j2 = make_joint(j, 'secret', 'code')
print(j2(5, 'code'))
print(j2(5, 'secret'))
print(j2(5, 'hax0r'))

print(j2(25, 'password'))
print(j2(5, 'secret'))
print(j(5, 'secret'))
print(w(5, 'hax0r'))
print(make_joint(w, 'hax0r', 'hello'))