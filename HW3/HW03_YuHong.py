#Question 1

def has_seven(k):
    # """Returns True if at least one of the digits of k is a 7, False otherwise.

    # >>> has_seven(3)
    # False
    # >>> has_seven(7)
    # True
    # >>> has_seven(2734)
    # True
    # >>> has_seven(2634)
    # False
    # >>> has_seven(734)
    # True
    # >>> has_seven(7777)
    # True
    # >>> from construct_check import check
    # >>> check(HW_SOURCE_FILE, 'has_seven',
    # ...       ['Assign', 'AugAssign'])
    # True
    # """

    # Write a recursive function has_seven that takes a positive integer n and 
    # returns whether n contains the digit 7. Use recursion - the tests will fail 
    # if you use any assignment statements.

    found7 = False

    if k == 0:
        return False
    elif (k%10) == 7:
        return True
    else:
        return has_seven(k//10)

#has_seven(9786)
#has_seven(1234)



#Question 2

def pingponghelp(n,state,num,counter):

    #Addition/Sub based on state
    if counter < n:
        #print(f"Number: {num}")
        #print(f"Count: {counter}")
        if has_seven(num) or (counter%7)==0:
            state = state * -1
            #print(f"New State: {state}")

        #print(f"State: {state}")
        if state == 1:
            #print("Check State 1")
            num+=1
            counter+=1
            #print("Looping Normal....")
            pingponghelp(n,state,num,counter)
        elif state == -1:
            #print("Check State -1")
            num-=1
            counter+=1
            #print("Looping invert...")
            pingponghelp(n,state,num,counter)


    #Final done deal        
    elif counter == n:
        print(f"Final Counter: {counter}")
        print(f"Final num: {num}")

def pingpong(n):
    state = 1
    num = 1
    counter = 1

    pingponghelp(n,state,num,counter)






pingpong(0)
#print(18%9)
