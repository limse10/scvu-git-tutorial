# Question 1 - Has Seven
def has_seven(K):
    if K % 10 == 7:
        return True
    if K < 10:
        return False
    else:
        return has_seven(K // 10)
    
# Question 1 Test
print("Question 1 Test")
print(has_seven(3))
print(False)
print(" ")
print(has_seven(2734))
print(True)
print(" ")
print(has_seven(2634))
print(False)
print(" ")
print(has_seven(734))
print(True)
print(" ")
print(has_seven(7777))
print(True)
print(" ")

# Question 2
def pingpong(n):
    def pingpong_helper(total, counter, direction):
        if counter == n:
            return total
        if has_seven(counter) or counter % 7 == 0:
            return pingpong_helper(total - direction, counter + 1, -1 * direction)
        return pingpong_helper(total + direction, counter + 1, direction)
    return pingpong_helper(1, 1, 1)



# Question 2 Test
print("Question 2 Test")
print(pingpong(7))
print(7)
print(" ")
print(pingpong(8))
print(6)
print(" ")
print(pingpong(15))
print(1)
print(" ")
print(pingpong(21))
print(-1)
print(" ")
print(pingpong(22))
print(0)
print(" ")
print(pingpong(30))
print(6)
print(" ")
print(pingpong(68))
print(2)
print(" ")
print(pingpong(69))
print(1)
print(" ")
print(pingpong(70))
print(0)
print(" ")
print(pingpong(71))
print(1)
print(" ")
print(pingpong(72))
print(0)
print(" ")
print(pingpong(100))
print(2)
print(" ")

