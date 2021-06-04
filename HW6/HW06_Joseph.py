# Question 1
class Fib():
    def __init__(self, value=0):
        self.value = value

    def next(self):
        next_fib = Fib()
        next_fib.previous = self.value
        if self.value == 0:
            next_fib.value = 1
        else:
            next_fib.value = self.value + self.previous
        return next_fib
    
    def __repr__(self):
        return str(self.value)

# Question 2
class VendingMachine:
    
    def __init__(self, product_name, price):
        self.name = product_name
        self.price = price
        self.wallet = 0
        self.stock = 0
    
    def restock(self, quantity):
        if quantity > 0:
            self.stock += quantity
            return f'Current {self.name} stock: {self.stock}'
    
    def deposit(self, amount):
        if amount > 0:        
            if self.stock == 0:
                return f'Machine is out of stock. Here is your ${amount}.'
            else:
                self.wallet += amount
                return f'Current balance: ${self.wallet}'

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        else:
            if self.wallet < self.price:
                check = self.price - self.wallet
                return f'You must deposit ${check} more.'
            else:
                self.stock -= 1
                change = self.wallet - self.price
                self.wallet -= self.wallet
                if change == 0:
                    return f'Here is your {self.name}.'
                else:
                    return f'Here is your {self.name} and ${change} change.'

    
# Question 1 Test
print("Question 1 Test")

start = Fib()

print(start)
print(0)
print("")

print(start.next())
print(1)
print("")

print(start.next().next())
print(1)
print("")

print(start.next().next().next())
print(2)
print("")

print(start.next().next().next().next())
print(3)
print("")

print(start.next().next().next().next().next())
print(5)
print("")

print(start.next().next().next().next().next().next())
print(8)
print("")

print(start.next().next().next().next().next().next())
print(8)
print("")

# Question 2 Test
print("Question 2 test")

v = VendingMachine('candy', 10)

print(v.vend())
print('Machine is out of stock.')
print("")

print(v.deposit(15))
print('Machine is out of stock. Here is your $15.')
print("")

print(v.restock(2))
print('Current candy stock: 2')
print("")

print(v.vend())
print('You must deposit $10 more.')
print("")

print(v.deposit(7))
print('Current balance: $7')
print("")

print(v.vend())
print('You must deposit $3 more.')
print("")

print(v.deposit(5))
print('Current balance: $12')
print("")

print(v.vend())
print('Here is your candy and $2 change.')
print("")

print(v.deposit(10))
print('Current balance: $10')
print("")

print(v.vend())
print('Here is your candy.')
print("")

print(v.deposit(15))
print('Machine is out of stock. Here is your $15.')
print("")

w = VendingMachine('soda', 2)

print(w.restock(3))
print('Current soda stock: 3')
print("")

print(w.restock(3))
print('Current soda stock: 6')
print("")

print(w.deposit(2))
print('Current balance: $2')
print("")

print(w.vend())
print('Here is your soda.')
print("")


print("\a\a\a\a\a\a\a\a\a\a\a")