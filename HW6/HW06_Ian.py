#QN1
'''class Fib():
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
        if self.value == 0:
            total = Fib(1)
        else:
            total = Fib(self.value + self.previous)      
        total.previous = self.value
        return total

    def __repr__(self):
        return str(self.value)
'''
#QN2
'''class VendingMachine:
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
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.stock = 0
        self.balance = 0
    
    def deposit(self, amount):
        if self.stock == 0:
            return "'Machine is out of stock. Here is your $" + str(amount) + ".'"
        else:
            self.balance = self.balance + amount 
            return "'Current balance: $" + str (self.balance) + "'"


    def restock(self, restock_value):
        self.stock = self.stock + restock_value 
        return "'current " + str(self.item) + " stock: " + str(self.stock) + "'"

    def vend(self):
        if self.stock == 0:
            if self.balance == 0:
                return "'Machine is out of stock.'"
        elif self.stock >= 1:
            if self.balance < self.price:
                return "'You must deposit $" + str(self.price - self.balance) + " more.'"
            elif self.balance > self.price:
                change = self.balance - self.price
                self.balance = 0
                self.stock = self.stock - 1
                return "'Here is your " + str(self.item) + " and $" + str(change) + " change.'"
            else:
                self.balance = 0
                self.stock = self.stock - 1
                return "'Here is your " + str(self.item) + "'"'''
