def checkHashrate(bigString):
    i = 0 
    acceptedSharesCount = 0 
    trigger = False 
    totalHashrate = 0 
    checkAgainst = ""
    dayCount = 0
    
    while i < len(bigString):
        #print (bigString[i:i+8])
        if bigString[i:i+8] == "Accepted":
            acceptedSharesCount += 1 
            trigger = True 
            commaCheck = 0 
        if trigger == True:
            if bigString[i] == ",":
                commaCheck += 1 
            if commaCheck == 2:
                temp = bigString[i+2:i+9]
                for x in range (len(temp)):
                    if temp[x] == " ":
                        temp = temp[:x]
                        break
                hashrate = float(temp)
                trigger = False 
                totalHashrate += hashrate
        
        if bigString[i:i+7] == "[2018-0":
            if checkAgainst == "":
                checkAgainst = bigString[i:i+11]
                
            if bigString[i:i+11] != checkAgainst:
                dayCount += 1 
                checkAgainst = bigString[i:i+11]

        
        i += 1  
   
    returnStr = "Total Hashrate: " + str(round(totalHashrate))
    returnStr += " Shares: " + str(acceptedSharesCount)
    returnStr += " Average: " + str(round(totalHashrate/acceptedSharesCount))
    returnStr += " Days: " + str(dayCount)
    
    return returnStr       

f = open("nohup.out", "r")
bigString = f.read()
f.close() 

input("Vps Name ")

print(checkHashrate(bigString))