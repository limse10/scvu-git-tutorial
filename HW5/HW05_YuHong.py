#Question 5

#Define a function make_counter that returns a counter function, which takes a string and returns the number of times that the function has been called on that string
def make_counter():
    # """Return a counter function.

    # >>> c = make_counter()
    # >>> c('a')
    # 1
    # >>> c('a')
    # 2
    # >>> c('b')
    # 1
    # >>> c('a')
    # 3
    # >>> c2 = make_counter()
    # >>> c2('b')
    # 1
    # >>> c2('b')
    # 2
    # >>> c('b') + c2('b')
    # 5
    # """
    # "*** YOUR CODE HERE ***"
    record = dict()

    def counter(word):
        if word not in record:
            record[word] = 1
            print(record[word])
            #return record[word]
            #print(f"New Record: {record}")
        else:
            occur = record[word] + 1
            record[word] = occur
            print(occur)
            #return occur
    
    return counter

# c = make_counter()
# c('a')


#Question 6

#Write a function make_fib that returns a function that returns the next Fibonacci number each time it is called. 
# (The Fibonacci sequence begins with 0 and then 1, after which each element is the sum of the preceding two.) 
# Use a nonlocal statement!

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
    num1 = 0
    num2 = 1

    def fibber():
        nonlocal num1, num2
        #print(num1,num2)
        result = num1
        tempNum = num2
        num1 = num2
        num2 = result + num2
        #print(result)
        return result

    return fibber

# fib = make_fib()
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())

#Question 7
 # Write a version of the make_withdraw function that returns password-protected withdraw functions. 
# That is, make_withdraw should take a password argument (a string) in addition to an initial balance. 
# The returned function should take two arguments: an amount to withdraw and a password.

# A password-protected withdraw function should only process withdrawals that include a password that matches the original. 
# Upon receiving an incorrect password, the function should:

# Store that incorrect password in a list, and
# Return the string 'Incorrect password'.
# If a withdraw function has been called three times with incorrect passwords p1, p2, and p3, then it is locked. 
#  All subsequent calls to the function should return:
# "Your account is locked. Attempts: [<p1>, <p2>, <p3>]"
# The incorrect passwords may be the same or different:

def make_withdraw(balance, password):

    record = []

    def withdraw(amount, pwd):
        nonlocal balance, password, record

        if len(record) >= 3:
            msg = f"You account is locked. Attempts: {record}"
            return msg

        elif (pwd == password):
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance = balance - amount
                msg = f"Remaining funds: {balance}"
                return msg

        else:
            record.append(pwd)
            triesLeft = 3 - len(record)
            msg = f"Incorrect Password. Remaining tries: {triesLeft}"
            return msg


    return withdraw

# w = make_withdraw(100,"pass")
# print(w(25,"pass"))
# print(w(1000,"pass"))
# print(w(25,"pawd"))
# print(w(25,"pawd"))
# print(w(25,"pa"))
# print(w(25,"pasdd"))
# print(w(25,"pass"))

#Question 8
def make_joint(withdraw, old_password, new_password):

    def join_withdraw(amount, pwd):
        if pwd == new_password:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, pwd)

    return join_withdraw

# w = make_withdraw(100,"pass")
# mj = make_joint(w,"pass","pass2")
# print(mj(25,"pass3"))
# print(mj(25,"pass4"))
# print(mj(25,"pass5"))
# print(mj(25,"pass6"))