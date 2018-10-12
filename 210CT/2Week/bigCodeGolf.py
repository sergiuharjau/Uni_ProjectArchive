n = 5

def readMatrix(file):
    """Reads matrices from given file, returns 2d array"""
    file1 = open(file, "r")
    rawData = file1.readlines()

    array2D = [[None for x in range(n)] for y in range(n)]
 
    j = 0
    for line in rawData:  
        i = 0 
        for element in line:
            if element != " ":
                if i == n:
                    break
                array2D[j][i] = element
                i+= 1 
        j+= 1 
    return array2D

def printState(array2D):
    """Prints the state of given array2D to terminal"""
    for i in range(len(array2D)):
        for j in range(len(array2D)):
            print(array2D[i][j] , end = " ")
        print("")

def advanceState(array2D):
    """Advances the state"""
    newArray2D = [[None for x in range(n)] for y in range(n)]
    exclude = [] 
    
    for x in range(len(array2D)):
        for y in range(len(array2D)):
            
            if (x,y) in exclude:
                continue
                
            if array2D[x][y] == "H":
                newArray2D[x][y] = "H"
            
            elif array2D[x][y] == "I": #infected becomes faded
                newArray2D[x][y] = "F"
           
                for m in range(-1,2):
                    for k in range(-1,2):
                        if m==k or m==-k: 
                            continue
                        try: 
                            if array2D[x+m][y+k] == "H":
                                newArray2D[x+m][y+k] = "I"
                                exclude.append((x+m,y+k))
                        except:
                            pass

            elif array2D[x][y] == "F": #faded becomes healthy 
                newArray2D[x][y] = "H"
    
    return newArray2D

if __name__ == "__main__":
    print("")
    print("Please use the file \"i\" for your input.")
    
    array2D = readMatrix("i")
    generations = int(input("How many generations? "))

    print("Gen 0: ")
    printState(array2D)
    input("")
    
    for i in range(generations):
        array2D = advanceState(array2D)
        
        print("Gen " + str(i +1) + ":")
        printState(array2D)
        input("")    
         
#2800 - first try     

#2200 - optimized code 

#1800 - no comments / whitespace

#1682 - more whitespace 

#1352 - variable/function names

#929  - 1 space indentation

#889  - changed output - still correct

#870  - deleted one function, hardcoded now

#825  - hardcoded another function. hell is real. 

#817  - renamed input.txt to i 