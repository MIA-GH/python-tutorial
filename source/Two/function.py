# # # function

def functionName():
    '''Your code goes here'''
    pass

# def printNumber():
#     print("2")
#     return ''

# myNumber = printNumber()
# print(myNumber)

def printMyNumber(num1, num2):
    print(str(num1), str(num2))


# print(functionName.__name__)
# print(functionName.__doc__)

# printMyNumber(4, 4)

# # # returns a value
# you can return bool, string, float, ...
def addNumbers(num1, num2):
    return num1 + num2

def isPrime(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

print(addNumbers(3,4))

# print(isPrime(7)) # this should be true
# print(isPrime(4)) # this should be false
