"""
2. Read from the keyboard a list of positive integers, for example: 1, 4, 7, 9
a. Write a function that prints the binary representation of the numbers in the list, for the example
above it is: 1: 0001 4: 0100 7: 0111 9: 1001
b. Print the numbers from the previous list that are palindromes. For example, 9: 1001 is a
palindrome.
c. Remove all the numbers in the list whose binary representation is a palindrome and print the list
after their removal.
"""
#Works as intended.

def receiveInput():
    """Input a list of user chosen size. Positive integers only."""
    listSize = int(input("How many numbers? "))
    
    if listSize < 0 : 
        raise Exception("Negative numbers not allowed.")
    
    inputList = [None] * listSize
    
    for i in range(listSize):
        inputList[i] = int(input("Number " + str(i+1) + ": "))
        
    return(inputList)

def makeListBinary(numberList): 
    
    binaryList = [None] * len(numberList)
    
    currentMax = 0 
    
    for i in range(len(numberList)):
        strRepr = bin(numberList[i])[2:] # 2 = 0b10
                                 # gets rid of "0b" 
        binaryList[i] = strRepr 
        
        if len(strRepr) > currentMax:
            currentMax = len(strRepr)
    """
    for i in range(len(binaryList)):
        if len(binaryList[i]) < currentMax:
            padding = "0" * (currentMax - len(binaryList[i]))
            binaryList[i] = padding + binaryList[i]
      """   #Padding   
    return (binaryList)

def palindromeCheck(binaryList):
    """Returns a list of palindromes from given list."""
    
    palindromes = [] 
    
    for element in binaryList:
        
        originalElement = element
        
        while len(element) >= 0:
            if len(element) == 1 or len(element) == 0:
                palindromes.append(originalElement)
                break
            else:
                if element[0]==element[len(element)-1]:
                    element = element[1:len(element)-1]
                else:
                    break
                
    return(palindromes)

def removePalindromes(palindromes, binaryList):
    
    for element in palindromes:
        binaryList.remove(element)
        
    return binaryList

if __name__ == "__main__":
    
    numberList = receiveInput() 
    
    #print(numberList)
    
    binaryList = makeListBinary(numberList)
    
    print("")
    print("Numbers in binary: " + str(binaryList) )
    
    palindromes = palindromeCheck(binaryList)
    
    print("Palindromes: " + str(palindromes) )
    
    noPalindromes = removePalindromes(palindromes, binaryList)
    
    print("List without palindromes: " + str(noPalindromes) )
    print("")