# Question 5
def make_counter():
    count = 0
    count_list = []
    def counter(x):
        nonlocal count, count_list
        count_list.append(x)
        count = count_list.count(x)
        return count
    return counter
    

# Question 6
def make_fib():
    first = 0
    second = 1
    third = 1
    count = 0
    def f():
        nonlocal first, second, third, count
        count += 1
        if count == 1:
            return 0
        elif count == 2:
            return 1
        third = first + second
        first = second
        second = third

        return third
    return f


# Question 7 
def make_withdraw(balance, password):
    wronglist = []
    password1 = password
    
    def withdraw(amount, password):
        nonlocal balance, wronglist
        if len(wronglist) < 3 and password == password1:
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance -= amount
            return balance
        elif len(wronglist) == 3 and password == password1:
            return f"Your account is locked. Attempts: {wronglist}"
        else: 
            if len(wronglist) < 3:
                wronglist.append(password)
                return 'Incorrect password'
            elif len(wronglist) == 3:
                return f"Your account is locked. Attempts: {wronglist}"
                
        return balance
    return withdraw

# Question 8 
def make_joint(withdraw, old_password, new_password):
    check = withdraw(0, old_password)
    if type(check) == str:
        return check
    else:
        def withdraw_joint(amount, joint_password):
            if joint_password == new_password:
                return withdraw(amount, old_password)
            else:
                return withdraw(amount, joint_password) 
        return withdraw_joint
    


# Question 5 Test
print("question 5 test")
c = make_counter()

print(c('a'))
print(1)
print ("")

print(c('a'))
print(2)
print ("")

print(c('b'))
print(1)
print ("")

print(c('a'))
print(3)
print ("")

c2 = make_counter()

print(c2('b'))
print(1)
print ("")

print(c2('b'))
print(2)
print ("")

print(c('b') + c2('b'))
print(5)
print ("")

# Question 6 Test
print("question 6 test")

fib = make_fib()

print(fib())
print(0)
print ("")

print(fib())
print(1)
print ("")

print(fib())
print(1)
print ("")

print(fib())
print(2)
print ("")

print(fib())
print(3)
print ("")

fib2 = make_fib()

print(fib() + sum([fib2() for _ in range(5)]))
print(12)
print ("")

# Question 7 Test
print("question 7 test")

w = make_withdraw(100, 'hax0r')

print(w(25, 'hax0r'))
print(75)
print ("")

error = w(90, 'hax0r')
print (error)
print('Insufficient funds')
print ("")

error = w(25, 'hwat')
print (error)
print ('Incorrect password')
print ("")

new_bal = w(25, 'hax0r')
print(new_bal)
print (50)
print ("")

print(w(75, 'a'))
print('Incorrect password')
print ("")

print(w(10, 'hax0r'))
print (40)
print ("")

print(w(20, 'n00b'))
print ('Incorrect password')
print ("")

print(w(10, 'hax0r'))
print("Your account is locked. Attempts: ['hwat', 'a', 'n00b']")
print ("")

print(w(10, 'l33t'))
print("Your account is locked. Attempts: ['hwat', 'a', 'n00b']")
print ("")

print(type(w(10, 'l33t')) == str)
print(True)
print ("")

# Question 8 Test
print ("question 8 test")

w = make_withdraw(100, 'hax0r')

print(w(25, 'hax0r'))
print(75)
print ("")

print(make_joint(w, 'my', 'secret'))
print('Incorrect password')
print ("")

j = make_joint(w, 'hax0r', 'secret')

print(w(25, 'secret'))
print('Incorrect password')
print ("")

print(j(25, 'secret'))
print(50)
print ("")

print(j(25, 'hax0r'))
print (25)
print ("")

print(j(100, 'secret'))
print('Insufficient funds')
print ("")

j2 = make_joint(j, 'secret', 'code')

print(j2(5, 'code'))
print(20)
print ("")

print(j2(5, 'secret'))
print(15)
print ("")

print(j2(5, 'hax0r'))
print(10)
print ("")

print(j2(25, 'password'))
print('Incorrect password')
print ("")

print(j2(5, 'secret'))
print("Your account is locked. Attempts: ['my', 'secret', 'password']")
print ("")

print(j(5, 'secret'))
print("Your account is locked. Attempts: ['my', 'secret', 'password']")
print ("")

print(w(5, 'hax0r'))
print("Your account is locked. Attempts: ['my', 'secret', 'password']")
print ("")

print(make_joint(w, 'hax0r', 'hello'))
print("Your account is locked. Attempts: ['my', 'secret', 'password']")
print ("")