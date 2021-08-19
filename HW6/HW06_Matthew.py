# Object Oriented Programming

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
        if self.value == 0: 
            a = Fib(1)
            a.prev = self.value
            return a
        else: 
            a = Fib(self.value + self.prev)
            a.prev = self.value
            return a
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
    def __init__(self, good, price):
        self.good = good
        self.price = price
        self.stock = 0
        self.balance = 0
    
    def vend(self): 
        if self.stock == 0: 
            return 'Machine is out of stock.'
        else: 
            if self.balance < self.price: 
                debt = self.price - self.balance
                return f'You must deposit ${debt} more.'
            elif self.balance == self.price: 
                self.stock = self.stock - 1
                self.balance = 0
                return f'Here is your {self.good}.'
            elif self.balance > self.price: 
                self.stock = self.stock - 1
                change = self.balance - self.price
                self.balance = 0
                return f'Here is your {self.good} and ${change} change.'

    def deposit(self, deposit): 
        if self.stock == 0: 
            return f'Machine is out of stock. Here is your ${deposit}.'
        else: 
            self.balance = self.balance + deposit
            return f'Current balance: ${self.balance}.'

    def restock(self, restock): 
        self.stock = self.stock + restock
        return f'Current {self.good} stock: {self.stock}'