"""
1. Write a function that takes an input a list of numbers and outputs a list of all numbers in the original
list that are Kaprekar numbers. A Kaprekar number is a non-negative integer, the representation of
whose square can be split into two parts that add up to the original number. For example, 45 is a
Kaprekar number, as 452 = 2025 𝑎𝑛𝑑 20 + 25 = 45. 9 is also a Kaprekar number, as 9^2 =
81 𝑎𝑛𝑑 8 + 1 = 9.
"""
#Works as intended.

from b2 import receiveInput

def testNumber(number):
    """Tests if a number is Kaprekar. Returns True/False"""
    i=1 
    numberSquared = number * number 
    
    while numberSquared // i > 0: 
        if (numberSquared // i) + (numberSquared % i) == number:
            return True 
        else:
            i *= 10 
            
    return False         

if __name__ == "__main__":
    numberList = receiveInput() 
    
    for element in numberList:
        print(str(element) + " " + str(testNumber(element)))
