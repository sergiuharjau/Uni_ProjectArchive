def getInput():
    """Asks for user input. Returns a tuple of (list,target)."""
    print("Input your numbers. Write 'exit' to stop.")
    userList = [] 
    while True:
        userInput = input()
        if userInput == "exit":
            break
        else:
            userList.append(int(userInput))
    return userList, int(input("Target number? "))

def findElement(numberList, target):
    """Recursively looks for target in numberList. Returns True/False"""
    if len(numberList) == 0:
        return False 
    if target == numberList[0]:
        return True 
    else:
        return findElement(numberList[1:], target)

if __name__ == "__main__":
    
    numberList, target = getInput()
    
    print(findElement(numberList, target))
    
    