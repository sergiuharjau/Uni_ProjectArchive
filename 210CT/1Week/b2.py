"""
2. Check if a 3 digit number is an Armstrong number. An Armstrong number of three digits is an integer
such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an
Armstrong number since 3**3 + 7**3 + 1**3 = 371.
Input: a number, such as 371
Output: “Yes” if the number is an Armstrong number, “No” if the number is not an Armstrong number.
"""
#Works as intended.

def isArmstrong(number):
    
    originalNumber = number 
    result = 0 
    
    while number > 0:
        result += (number % 10) ** 3 
        number = number // 10 
    
    if result == originalNumber:
        return True 
    else:
        return False 


if __name__ == "__main__":
    number = int(input("Number: ")) 
    print(isArmstrong(number))