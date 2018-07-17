question = input("\nWhat shall we vote on today? ")
answersNr = int(input("\nHow many options are there? "))
numberOfVoters = int(input("\nHow many voters? "))

optionsList = [] 

for i in range (0, answersNr): 
    optionsList.append(input("\nOption " + str(i+1) + "? "))
    print("")    

listFinal = []

input("\nPress enter to start voting.")

for voter in range (0, numberOfVoters):
    listFinal.append([])
                    #creates empty choice list for voter
    print("\n\nVoter " + str(voter + 1) + "\n------------------")

    print(question)
    
    i = 1
    for option in optionsList: 
        print(str(i)+". " + option)
        i = i + 1 
    
    answer = input("What are your choices, ranked on your preference?\n") 
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for character in answer:
        if character in numbers:
            if int(character) > answersNr or int(character) < 0:
                pass #avoids trolls
            elif character in listFinal[voter]:
                pass #avoids duplicates
            else:
                listFinal[voter].append(character)
                            #populates choice list 

print(listFinal)
