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
        next_fib = Fib()
        next_fib.prev = self.value  
        if self.value == 0:
            next_fib.value = 1 
        else: 
            next_fib.value = self.value + self.prev
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
        self.product = product
        self.price = price  
        self.balance =0 
        self.stock = 0
    
    def restock(self, quantity): 
        self.stock += quantity 
        return f"Current {self.product} stock: {self.stock}"
    
    def deposit(self, amount): 
        if self.stock == 0: 
            return f"Machine is out of stock. Here is your ${amount}."
        else: 
            self.balance += amount 
            return f"Current balance: ${self.balance}"
   
    def vend(self):
        if self.stock == 0: 
            return "Machine is out of stock."
        elif self.balance > self.price: 
            self.stock-= 1 
            extra_money= self.balance - self.price
            self.balance= 0 
            return f"Here is your candy and ${extra_money} change."
        elif self.balance < self.price: 
            need_money= self.price - self.balance 
            return f"You must deposit ${need_money} more."
        else: 
            self.balance = 0
            self.stock-=1 
            return f"Here is your {self.product}."