# Object Oriented Programming


    class Fib():
        def __init__(self, value=0):
            self.value = value

        def next(self):
            if self.value == 0:
                result = Fib(1)
            else:
                result = Fib(self.value + self.previous)
            result.previous = self.value
            return result

        def __repr__(self):
            return str(self.value)

class VendingMachine:
    def __init__(self,food_item,price):
        self.item=food_item
        self.cost=price
        self.stock=0
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        if self.stock==0:
            self.balance=self.balance-amount
            return("Machine is out of stock. " + " Here is your $" + str(amount))
        else:
            return("Current balance: "+str(self.balance))
    def restock(self,quantity):
        self.stock=self.stock+quantity
        return("Current "+ str(self.item)+" stock: "+str(self.stock))
    def vend(self):
        if self.stock==0:
            return("Machine is out of stock.")
        elif self.balance<self.cost:
            short_of=self.cost-self.balance
            return("You must deposit: $"+str(short_of)+" more.")
        elif self.balance==self.cost:
            self.balance=self.balance-self.cost
            self.stock -= 1
            return("Here is your "+str(self.item)+".")
        else:
            self.balance=self.balance-self.cost
            change_given=self.balance
            self.stock-=1
            return("Here is your "+str(self.item)+" and $"+str(change_given)+" change")
