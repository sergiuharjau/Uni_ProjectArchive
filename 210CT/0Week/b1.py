"""
1. Write a function that deletes a substring from a given character string, specifying the beginning
position and the length of the substring.
"""
#Works as inteded.

def deleteSubString(mainString, pos, length):
    
    newString = mainString[:pos-1] + mainString[pos+length-1:]
    
    return (newString)

def receiveInput():
    givenString = input("Give a string: ")

    position = int(input("Position to truncate at: "))

    length = int(input("Length of truncation: "))
    
    return (givenString, position, length)

if __name__ == "__main__":
    
    givenString, position, length = receiveInput()
    
    newString = deleteSubString(givenString, position, length)

    print(newString)