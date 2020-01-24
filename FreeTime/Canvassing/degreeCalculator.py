def getInput():
    secondYear = [] #list of tuples (Grade, Credits)
    thirdYear = [] 
    passedHalf = False

    for line in open("degree_input.txt", "r").readlines():

        if line == "###\n":
            passedHalf = True
            continue

        if passedHalf:
            gradeCredit = line[:-1].split(" ")
            thirdYear.append( (float(gradeCredit[0]), float(gradeCredit[1])) )
        else:  
            gradeCredit = line[:-1].split(" ")         
            secondYear.append( (float(gradeCredit[0]), float(gradeCredit[1])) )

    return secondYear, thirdYear 

def perCreditAverage(givenList): #list of tuples (Grade, Credits)
    totalGrades = 0 
    totalCredits = 0
    #print("Marks we're averaging: ", givenList)

    for element in givenList:
        totalGrades += element[0] * element[1]
        totalCredits += element[1]

    return round(totalGrades/ totalCredits, 2)

def findMinimumOfCredits(givenList, credits):

    minimum = [100,100]
    for element in givenList:
        if element[0] < minimum[0] and element[1]==credits:
            minimum = element

    if minimum[0] == 100:
        return [0,0]
    return minimum

def getBestCredits(givenList):
    """Returns best credits-20 out of givenList """
    worst20Module = (findMinimumOfCredits(givenList, 20))
    
    bad10Module = findMinimumOfCredits(givenList, 10)
    givenList.remove(bad10Module) #removing to find second bad

    secondBad10Module = findMinimumOfCredits(givenList, 10)
    twoBad10Modules = [bad10Module, secondBad10Module]

    print("Worst 20 credit module: ", worst20Module)
    print("Worst two 10 credit modules: " + str(twoBad10Modules) + " Average: " + str(perCreditAverage(twoBad10Modules)))

    twoBadTotalCredits = twoBad10Modules[0][1] + twoBad10Modules[1][1]

    if worst20Module[0] > perCreditAverage(twoBad10Modules) and twoBadTotalCredits == 20:
        print("Removing your worst two modules: ", twoBad10Modules)
        givenList.remove(secondBad10Module)
    else:
        print("Removing your worst module: ", worst20Module)
        givenList.append(bad10Module) #to undo the search of the second 
        givenList.remove(worst20Module)

    return givenList 

if __name__ == "__main__":
    second, third = getInput()

    print("Second Year: ", second)
    print("Third Year: ", third)

    print("\nProcessing First Scenario: ")
    firstScenario = perCreditAverage(getBestCredits(third))
    print("First scenario grade: ", firstScenario)

    secondAgain, thirdAgain = getInput()
    print("\nProcessing Second Scenario")
    secondScenario = perCreditAverage(getBestCredits(secondAgain+thirdAgain))
    print("Second scenario grade: ", secondScenario)

    if firstScenario > secondScenario:
        print("\nThird year is better than second. Here are your best 100 credits averaged:")
        print(firstScenario)
    else:
        print("\nThird year is not as good. Here are your best 220 credits averaged from 2nd and 3rd year:")
        print(secondScenario)
    