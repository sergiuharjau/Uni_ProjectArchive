"""
1. The factorial for a non-negative integer n, n!, is defined as: 0! = 1 n! = n * (n-1)! (n > 0). The input to
your program consists of several lines, each containing two non-negative integers, n and m, both less
than 2^31. For each input line, output a line stating whether or not m divides n!.
Example input:
6 9
6 27
Example output:
9 divides 6!
27 does not divide 6!
"""
#Works as intended. 

def getFactorial(number):
    
    result = 1  
    while number > 0:
        result *= number 
        number -= 1  
    return result 
    
def divideCheck(number1, number2):
    """Decides if number1 divides number2."""
    if number2 % number1 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    
    number1 = int(input("Number1: "))
    number2 = int(input("Number2: "))
    
    if divideCheck(number2, getFactorial(number1)) == True:
        print(str(number2) + " divides " + str(number1) + "!")
    else:
        print(str(number2) + " does not divide " + str(number1) + "!")

