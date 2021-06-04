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
    "*** YOUR CODE HERE ***"
    # Added a class attribute to keep track of the previous term
    terms = []

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        self.terms.append(self.value)
        if self.value == 0:
            next = Fib(1)
        else:
            self.previous = self.terms[len(self.terms) - 2]
            next = Fib(self.value + self.previous)
        return next

    def __repr__(self):
        return str(self.value)

# Tests
def main():
    start = Fib()
    print(f"{start}")
    print(f"{start.next()}")
    print(f"{start.next().next()}")
    print(f"{start.next().next().next()}")
    print(f"{start.next().next().next().next()}")
    print(f"{start.next().next().next().next().next()}")
    print(f"{start.next().next().next().next().next().next()}")
    print(f"{start.next().next().next().next().next().next()}")

if __name__ == "__main__":
    main()

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

    :) VendingMachine passes all doctests for candy
    :) VendingMachine passes all doctests for soda
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0
        self.amount = 0
    
    def deposit(self, input):
        if self.stock == 0:
            return f"Machine is out of stock. Here is your ${input}."
        elif self.stock > 0:
            self.amount = self.amount + input
            return f"Current balance: ${self.amount}"
    
    def restock(self, quantity):
        self.stock = self.stock + quantity
        return f"Current {self.name} stock: {self.stock}"

    def vend(self):
        # Check for self.stock and self.amount. Two cases for change.
        if self.stock == 0:
            return "Machine is out of stock."
        else:
            if self.amount < self.price:
                balance = self.price - self.amount
                return f"You must deposit ${balance} more."
            elif self.amount == self.price:
                self.amount = 0
                self.stock = self.stock - 1
                return f"Here is your {self.name}."
            elif self.amount > self.price:
                change = self.amount - self.price
                self.amount = 0
                self.stock = self.stock - 1
                return f"Here is your {self.name} and ${change} change."