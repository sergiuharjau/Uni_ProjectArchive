def readMatrix(file):
    """Reads matrices from given file, returns list of 2d arrays"""
    file1 = open(file, "r")
    rawData = file1.readlines()
    file1.close() 
    
    n = round(len(rawData[0])/2) 
    
    matrix2D = [[None for x in range(n)] for y in range(n)] 
    
    j = 0
    for line in rawData:  
        i = 0 
        for element in line:
            if element != " ":
                if i == n:
                    break
                matrix2D[j][i] = element
                i+= 1 
        j+= 1 
    
    return matrix2D

def removeFirstMatrix(file):
    """Removes first matrix from given file, so we can work on the next."""
    file1 = open(file, "r") #In the future this function can just reside in readMatrix() 
    
    rawData = file1.readlines() 
    
    n = round (len(rawData[0])/2)
    
    newData = rawData[n+1:]
    
    file1 = open(file, "w")

    for line in newData:
        file1.write(line)
    file1.close()

def spiralPrint(a) : 
    k = 0; l = 0
    m = n = int(len(a))

    while (k < m and l < n) : 
  
        for i in range(l, n) : 
            print(a[k][i], end = " ")      
        k += 1
        print("") 
  
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
        print("")       
        n -= 1

        if (k < m) :       
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
            m -= 1
            print("")  

        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
            l += 1
            print("")
        
if __name__ == "__main__":

    # open matrix from file 
    # 
    # process it, apply every function 
    # 
    # delete first matrix
    # 
    # open matrix from file, rinse an repeat 
    # 
    # 
    matrix2D = readMatrix("matrix.txt")
    spiralPrint(matrix2D)