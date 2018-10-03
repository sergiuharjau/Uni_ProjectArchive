def codeOnly(filename):
    f1=open(filename, "r")
    bigString=f1.read()
    listOfLines=bigString.split("\n")
    for line in listOfLines:
        i=-1
        for character in line:
            i+=1
            if character == "#":
                line=line[:i]
        print(line)
        
        
codeOnly("primeFinder.py")