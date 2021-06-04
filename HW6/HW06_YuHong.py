#Question 1

# Implement the next method of the Fib class. For this class, the value attribute is a Fibonacci number. 
# The next method returns a Fib instance whose value is the next Fibonacci number. The next method should take only constant time.

# Note that in the doctests, nothing is being printed out. Rather, each call to .next() returns a Fib instance, 
# which is represented in the interpreter as the value of that instance (see the __repr__ method).
# Hint: Keep track of the previous number by setting a new instance attribute inside next.

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

        if hasattr(self,"oldVal"):
            newVal = self.oldVal + self.value
        else:
            newVal = self.value + 1
            # self.oldVal = self.value
            # # self.oldVal = self.value
            # # self.value += 1
        test = Fib(newVal)
        test.oldVal = self.value

        return test
            


    def __repr__(self):
        return str(self.value)

# start = Fib()
# print(start)
# print(start.next())
# print(start.next().next())
# print(start.next().next().next())
# print(start.next().next().next().next().next())
# print(start.next().next().next().next().next().next())

# Question 2
class VendingMachine:

    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.bal = 0
        self.stock = 0

    def vend(self):
        #Check stock
        if self.stock == 0:
            print("Machine is out of stock.")
        else:
            #Check if enuf money
            if self.bal < self.price:
                print(f"You must deposit ${self.price-self.bal} more.")
            else:
                #Reduce stock and balance
                self.stock = self.stock - 1
                self.bal = self.bal - self.price
                #check balance
                if self.bal == 0:
                    print(f"Here is your {self.item}.")
                #Change dispense
                else:
                    print(f"Here is your candy and ${self.bal} change")
                    self.bal = 0

    def deposit(self,cash):
        self.bal = self.bal + cash
        if self.stock == 0:
            print(f"Machine is out of stock. Here is your ${self.bal}")
            self.bal = 0
        else:
            print(f"Current balance: ${self.bal}")

    def restock(self, addStock):
        self.stock = self.stock + addStock
        print(f"Current {self.item} stock: {self.stock}")

# v = VendingMachine("candy",10)
# v.deposit(15)
# v.restock(2)
# v.vend()
# v.deposit(7)
# v.vend()
# v.deposit(5)
# v.vend()
# v.deposit(10)
# v.vend()
# v.deposit(15)

# w = VendingMachine('soda', 2)
# w.restock(3)
# w.restock(3)
# w.deposit(2)
# w.vend()


