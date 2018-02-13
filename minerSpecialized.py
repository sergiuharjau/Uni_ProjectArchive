import subprocess, time

daysPassed = 0

vpsName = "   COMPLETE ME      "

def checkHashrate(vpsName):
    i = 0
    acceptedSharesCount = 0
    trigger = False
    totalHashrate = 0
    checkAgainst = ""
    dayCount = 0

    f = open("10daysNH.txt", "r")
    bigString = f.read()
    f.close()

    while i < len(bigString):
        # print (bigString[i:i+8])
        if bigString[i:i + 8] == "Accepted":
            acceptedSharesCount += 1
            trigger = True
            commaCheck = 0
        if trigger == True:
            if bigString[i] == ",":
                commaCheck += 1
            if commaCheck == 2:
                temp = bigString[i + 2:i + 9]
                for x in range(len(temp)):
                    if temp[x] == " ":
                        temp = temp[:x]
                        break
                hashrate = float(temp)
                trigger = False
                totalHashrate += hashrate

        if bigString[i:i + 7] == "[2018-0":
            if checkAgainst == "":
                checkAgainst = bigString[i:i + 11]

            if bigString[i:i + 11] != checkAgainst:
                dayCount += 1
                checkAgainst = bigString[i:i + 11]

        i += 1

    returnStr = "\n" + vpsName + "\n"
    returnStr += " Total Hashrate: " + str(round(totalHashrate))
    returnStr += " Shares: " + str(acceptedSharesCount)
    returnStr += " Average: " + str(round(totalHashrate / acceptedSharesCount))
    returnStr += " Days: " + str(dayCount)

    return returnStr

def stopwatch(minutes):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < minutes:
        elapsed += 1 
        time.sleep(60)
i = 0

while True:
    p = subprocess.Popen("exec " + "(./cpuminer -a lyra2zoin -o stratum+tcp://zoi-pool3.chainsilo.com:3032 -u Greeny47.Joyent1 -p Joyent1) >> 10daysNH.txt", shell=True)
    stopwatch(3)                                                       #we're appending mining output to 10daysNH.txt
#waits 58 minutes then kill the process
    p.kill()
    stopwatch(0)
#waits 2 minutes then starts again

    daysPassed += 1
#since this is ran every hour, we add 1/24th of a day, so in 24 hours, we get a full day
    if daysPassed == 2:
        i += 1
#we're printing everything to the NOHUP of the python program.
        print(checkHashrate(vpsName))
#since we are in the same directory, we run the function, giving us the results
        print("We have just ran the hashrate counter for the past 10 days.")

        p = subprocess.Popen("mv 10daysNH.txt /root/10daysNH" +str(i)+ ".txt ", shell = True)
#we move the file completely, so when we start the mining, it creates a new empty file
        print("The 10daysNH file is now on /root/ and will be available forever hopefully")
#in 10 days, we will overwrite the file with a new one
        daysPassed = 0