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

    Implement the next method of the Fib class. For this class, the value attribute is a Fibonacci number. 
    The next method returns a Fib instance whose value is the next Fibonacci number. 
    The next method should take only constant time.

    Note that in the doctests, nothing is being printed out. 
    Rather, each call to .next() returns a Fib instance, which is represented in the interpreter 
    as the value of that instance (see the __repr__ method).

    Hint: Keep track of the previous number by setting a new instance attribute inside next.
    """
    
    def __init__(self, value=0):
        self.value = value
        #value=0 creates input for fib() but sets default to 0
    
    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            result = Fib(1)
        else:
            result = Fib(self.value + self.previous)
        result.previous = self.value
        return result

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
    'Current bal: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current bal: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current bal: $10'
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
    'Current bal: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    
    def __init__(self, item, price):
        self.item = item
        self.bal, self.stock = 0 , 0
        self.price = price

    def restock(self, n):
        self.stock += n
        return f'Current {self.item} stock: {self.stock}'

    def deposit(self, amount):
        if self.stock > 0:
            self.bal += amount
            return f'Current bal: ${self.bal}'
        else:
            return f'Machine is out of stock. Here is your ${amount}.'

    def vend(self):
        if self.stock > 0:
            if self.bal >= self.price:
                change = self.bal - self.price
                self.stock -= 1
                self.bal = 0
                if change == 0:
                    return f'Here is your {self.item}.'
                return f'Here is your {self.item} and ${change} change.'
            elif self.bal < self.price:
                return f'You must deposit ${self.price - self.bal} more.'
        else:
            return 'Machine is out of stock'
