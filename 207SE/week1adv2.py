def scanID(studentID):
    """Takes as input a student ID, returns desired digit"""
    desiredDigits = ["3", "4", "5", "6"] 
    for digit in str(studentID):
        if digit in desiredDigits:
            return (int(digit))
    return 3 

def receiveInput():
    """Returns name, sid string tuple"""
    name = input("Name? ")
    sid = input("StudentID? ")
    
    return name, sid 

def createOutput(name, sid):
    
    size = scanID(sid)
    i = 1
    name = name.replace(" ", "+")

    for letter in name:
        print(letter, end = " ")
        if i % size == 0:
            print()
        i += 1

    while (i-1) % size != 0:
        print("*", end = " ")
        i += 1
        
    print()
    
    
if __name__ == "__main__":
    name, sid = receiveInput()
    createOutput(name, sid)
    createOutput(name[::-1], sid) 