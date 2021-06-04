#question 5
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
        if dic.get(n) != None:
            dic[n] = dic.get(n) + 1 #assigning a value to the key which is n
            return dic.get(n) #returning new value to dict
        else:
            dic[n] = 1 #assigning a value 1 to key n
            return 1 #returning value 1 back to dict
    
    return d #must return function d back to make_counter 
c = make_counter()
print(c("a"))
print(c("b"))

#question 6
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
    a , b = 0, 1 
    def fib():
        nonlocal a, b
        result = a
        a, b = b, a+b
        return result
    
    return fib

fib = make_fib()
print(fib())
print(fib())
print(fib())    
print(fib())
print(fib())
fib2 = make_fib()
print(fib() + sum([fib2() for _ in range(5)]))

#question 7:
def make_withdraw(balance, password):
    l = []
    def withdraw(amount, word):
        nonlocal balance, password
        if len(l) != 3:
            if word == password:
                if amount > balance:
                    return "Insufficient Funds"
                else:
                    balance = balance - amount
                    return balance
            else:
                l.append(word)
                return "Incorrect Password"
        else:
            return "Your accoount is locked. Attempts:{}".format(l)
    
    return withdraw

#question 8
def make_joint(withdraw, old_password, new_password):
    a = withdraw(0, old_password) #store result of call withdraw 0
    if type(a) == int:
        def ass_password(amount, stupid):
            if stupid == new_password:
                return withdraw(amount, old_password)
            elif stupid == old_password:
                return withdraw(amount, old_password)
            else:
                return withdraw(amount, stupid)
        return ass_password
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