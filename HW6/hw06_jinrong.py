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
        # newFib = Fib()
        if self.value == 0:
            # newFib.value = 1
            newFib = Fib(1)
        else:
            newFib = Fib(self.value + self.a)
        # print(self.a)
        newFib.a = self.value
        # print(dir(newFib))
        # print(vars(newFib))
        return newFib

    def __repr__(self):
        return str(self.value)

start = Fib()
print(start)
print(start.next())
print(start.next().next())
print(start.next().next().next())
# print(start.next().next().next().next())
# print(start.next().next().next().next().next())
# print(start.next().next().next().next().next().next())
# print(start.next().next().next().next().next().next())

#02: Vending Machine
class VendingMachine:
    
    def __init__(self, product, price):
        self.stock = 0
        self.product = product
        self.price = price
        self.money = 0

    def vend(self):
        if self.stock > 0:
            if self.price > self.money:
                a = self.price - self.money
                return 'You must deposit ${} more.'.format(a)
            else:
                if self.money > self.price:
                    b = self.money - self.price
                    self.money = 0
                    self.stock -= 1
                    # print(self.money) = 12
                    return 'Here is your {} and ${} change.'.format(self.product, b)
                else:
                    self.money = 0
                    self.stock -= 1
                    return 'Here is your {}.'.format(self.product)
        else:
            return 'Machine is out of stock.'

    def deposit(self, money): #money
        if self.stock > 0:
            self.money = self.money + money
            return 'Current balance: ${}'.format(self.money)
        else:
            return 'Machine is out of stock. Here is your ${}.'.format(money)

    def restock(self, number): #number to restock
        self.stock = self.stock + number
        return 'Current {} stock: {}'.format(self.product,self.stock)
    

# v = VendingMachine('candy', 10)
# print(v.vend())
# print(v.deposit(15))
# print(v.restock(2))
# print(v.vend())
# print(v.deposit(7))
# print(v.vend())
# print(v.deposit(5))
# print(v.vend())
# print(v.deposit(10))
# print(v.vend())
# print(v.deposit(15))

# w = VendingMachine('soda', 2)
# print(w.restock(3))
# print(w.restock(3))
# print(w.deposit(2))
# print(w.vend())