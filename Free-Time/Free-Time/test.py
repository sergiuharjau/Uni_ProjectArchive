currentLevel = 0
humanLevel = 2 

while True: 
    print("--------------------")
    
    availableLevels = ["ground",1,2,3,4]
    
    print("Human level: " + str(humanLevel))
    if currentLevel == 0:
        currentLevel = "ground"    
    print("Lift level: " + str(currentLevel))  
    if currentLevel == "ground":
        currentLevel = 0 

    print("Available levels:", end = " ")
    for element in availableLevels:
        print(element, end=" ")
    print("")
    
    if currentLevel == humanLevel:
        nextLevel = input("Where do you want to go? ")
        if nextLevel == "ground":
            nextLevel = 0
        
        if int(nextLevel) > currentLevel: 
            print("Going up.")
        elif int(nextLevel) < currentLevel:
            print("Going down.")
        else:
            print("Uh.. We're already here.")
        currentLevel = int(nextLevel)
        humanLevel = currentLevel
        input("Press any key to proceed to your destination!")
    else: 
        input("Press enter to call the lift.")
        currentLevel += 1 
            
