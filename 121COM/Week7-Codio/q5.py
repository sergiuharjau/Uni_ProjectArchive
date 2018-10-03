def pager(filename):
    f1=open(filename,"r")
    bigString=f1.read()
    listLines=bigString.split("\n")
    i=-1
    for line in listLines:
        i+=1
        print(line)
        for x in range (1,100):
            if i==5*x:
                input("")

pager("words.txt")  