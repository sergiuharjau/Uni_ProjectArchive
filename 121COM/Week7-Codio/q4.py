def dictPrinter(inD):
    """Given dictionary inD this prints out the key-value pairs one per line, aligned on the colon"""
    
    # First we find the longest key
    m = 0
    for var in inD:
        size = len(str(var))
        if size>m:
            m = size
    
    # Then we print out pairs so colons align
    
    list1=list(inD)  #Since the list of a dict gives us all the keys
    list1.sort()    
    
            #sort them in ascending order, then use the for loop on the list
    for var in list1:
        keyStr = str(var)
        size = len(keyStr)
        print( keyStr + " "*(m-size) + " : " + str(inD[var]) )
    print("")
        
#stock = {'bananas': 31, 'oranges': 55, 'apples': 40, "pears":33}
#dictPrinter(stock)
        
eng2sp = { "one":"uno", "two":"dos", "three":"tres" }
dictPrinter(eng2sp)
        