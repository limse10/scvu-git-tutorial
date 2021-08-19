# Object Oriented Programming

class Fib():

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            result = Fib(1)
        else:
            result = Fib(self.value + self.prev)
        result.prev = self.value
        return result

    def __repr__(self):
        return str(self.value)


class VendingMachine: 

    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.balance = 0
        self.stock = 0

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.balance < self.price:
            difference = self.price - self.balance
            return f"You must deposit ${difference} more."
        if self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return f"Here is your {self.item} and ${change} change."
        self.balance = 0
        self.stock -= 1
        return f"Here is your {self.item}."

    def deposit(self, amount):
        if self.stock == 0:
            return f"Machine is out of stock. Here is your ${amount}."
        self.balance += amount
        return f"Current balance: ${self.balance}"
    
    def restock(self, new_stock):
        self.stock += new_stock
        return f"Current {self.item} stock: {self.stock}"