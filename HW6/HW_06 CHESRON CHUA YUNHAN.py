# Object Oriented Programming

from typing import NewType


class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        next_fib = Fib()
        if self.value == 0:
            next_fib.value = 1
        else:
            next_fib.value = self.value + self.previous
        next_fib.previous = self.value
        return next_fib

    def __repr__(self):
        return str(self.value)    
        


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        self.price = price
        self.product = product
        self.stock = 0
        self.amount = 0
    
    
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        diff = self.price - self.amount
        if diff > 0:
            return 'You must deposit ${0} more.'.format(diff)
        else:
            change = self.amount - self.price 
            self.stock -=1 
            self.amount = 0   #take out money before next person uses
            if change > 0:
                return "Here is your {0} and ${1} change.".format(self.product, change)
            else:
                return "Here is your {0}.".format(self.product)

    
    def deposit(self, n):
        if self.stock == 0:
            return "Machine is out of stock. Here is your ${0}.".format(n)
        else:
            self.amount += n
        return 'Current balance: ${0}'.format(self.amount)
        
   
   
    def restock(self, n):
        self.stock += n
        return "Current {0} stock: {1}".format(self.product, self.stock)

v = VendingMachine('candy', 10)
print(v.vend())
print(v.deposit(15))

            
