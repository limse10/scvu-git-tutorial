# Question 1

from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# for testing question 1
print(a_plus_abs_b(2, -3))
print(a_plus_abs_b(2, 3))

print(" ")

# Question 2 (Return x*x + y*y, where x and y are the two largest members of the positive numbers a, b, and c.)

def two_of_three(a, b, c):
    return a*a + b*b + c*c - min(a, b, c)*min(a, b, c)


# for testing question 2
print(two_of_three(1, 2, 3))
print(two_of_three(10, 2, 8))

print("  ")

# Question 3 
def largest_factor(n):
    for x in range(1,n)[::-1]:
        if n%x == 0:
            return x

# for testing question 3
print(largest_factor(15))
print(largest_factor(80))

print("  ")

# Question 4: part 1
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

# for testing question 4: part 1
print(if_function(True, 2, 3))
print(if_function(3>2, 3+2, 3-2))

print("  ")

# Question 4: part 2
def with_if_statement():
    if c():
        return t()
    else:
        return f()


def with_if_function():
    return if_function(c(), t(), f())


def c():
    return False

def t():
    print (1)

def f():
    print (2)

# for testing question 4: part 1
result = with_if_statement()
print(result)
result = with_if_function()
print(result)

print("  ")

# Question 5
def hailstone(n):
    
    count = 1
    assert n > 0
    print(n)
    if n > 1:
        if n%2 == 0:
            count += hailstone(n / 2) 
        else:
            count += hailstone((n * 3) +1)
    return count


# for testing question 5
a = hailstone(10)
print(a)
