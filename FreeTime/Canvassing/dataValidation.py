def validDate(date, lowerBoundary, upperBoundary):
    """Takes as in put a string dd/mm/yyyy. Returns True/False on validation"""
    if date[2] != "/" or date[5] != "/":
        return False 
    elif int(date[:2]) < int(lowerBoundary[:2]) or int(date[:2]) > int(upperBoundary[:2]):
        return False 
    elif int(date[3:5]) < int(lowerBoundary[3:5]) or int(date[3:5]) > int(upperBoundary[3:5]):
        return False
    elif int(date[6:]) < int(lowerBoundary[6:]) or int(date[6:]) > int(upperBoundary[6:]):
        return False
    
    return True

date = input("Date: ")
lowerBoundary = "01/01/1900"
upperBoundary = "31/12/2017"

print(validDate(date, lowerBoundary, upperBoundary))


