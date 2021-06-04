class Fib():
    """A Fibonacci number.
    >>> start = Fib()"""
 
    def __init__(self, value=0):
        self.value = value

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

start = Fib()
print(start)
print(start.next())
print(start.next().next())
print(start.next().next().next())
print(start.next().next().next().next())
print(start.next().next().next().next().next())
print(start.next().next().next().next().next().next())
print(start.next().next().next().next().next().next())

class VendingMachine:
        def __init__(self, product, price): #self is is
            self.stock = 0
            self.product = product
            self.price = price
            self.money = 0

        def deposit(self, money):
            if self.stock == 0:
                return "Machine is out of stock. Here is your ${}".format(money)
            else:
                self.money = self.money + money 
                return "Current Balance: ${}".format(self.money)

        def restock(self, stock):
            self.stock = self.stock + stock
            return "Current {} stock:{}".format(self.product, self.stock)

        def vend(self):
            if self.stock == 0:
                return "Machine is out of stock"
            else:
                if self.money == 0:
                    return "You must deposit ${} more".format(self.price)
                elif self.money < self.price:
                    a = self.price - self.money
                    return "You must depost ${} more".format(a)
                elif self.money == self.price:
                    return "Here is your {}".format(self.product)
                else:
                    b = self.money - self.price
                    self.money = 0
                    return "Here is your {} and ${} change".format(self.product, b)


                
v = VendingMachine('candy', 10)
print(v.vend())
print(v.deposit(15))
print(v.restock(2))
print(v.vend())
print(v.deposit(7))
print(v.vend())
print(v.deposit(5))
print(v.vend())
print(v.deposit(10))
print(v.vend())
print(v.deposit(15))

w = VendingMachine('soda', 2)
print(w.restock(3))
print(w.restock(3))
print(w.deposit(2))
print(w.vend())
