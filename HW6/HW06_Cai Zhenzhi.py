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
            next_fib = Fib(1)
            next_fib.past = 0
            return next_fib
        next_fib = Fib(self.value+self.past)
        next_fib.past = self.value
        return next_fib

    def __repr__(self):
        return str(self.value)

class fib2():
    terms = []

    def __init__(self,value=0):
        self.value =  value
    def next(self):
        self.terms.append(self.value)
        print(self.terms)
        if self.value == 0:
            self.terms = []
            next = fib2(1)
        else:
            self.previous = self.terms[len(self.terms)-2]
            next = fib2(self.value + self.previous)
        return next
    def __repr__(self):
        return str(self.value)
test = fib2()
print(test.next().next().next().next())
print(test.next().next().next().next())
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
    def __init__(self,item,price):
        self.item = item
        self.price = price
        self.balance = 0
        self.stock = 0
    
    def deposit(self,money):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $'+str(money)+'.'
        else:
            self.balance += money
            return 'Current balance: $'+str(self.balance)

    def restock(self,stock):
        self.stock += stock
        return 'Current '+self.item+' stock: '+str(self.stock)


    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return 'Here is your '+self.item+' and $'+str(change)+' change.'
        elif self.balance == self.price:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return 'Here is your '+self.item+'.'
        else:
            return 'You must deposit $'+str(self.price-self.balance)+' more.'
    

