def greater_than(x, y): #user-defined function called greater-than
    if x > y:
        return True
    else:
        return False

#Main section

a = 10
b = 6
result = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
