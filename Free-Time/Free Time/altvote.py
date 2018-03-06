question = input("What shall we vote on today? ")
answersNr = int(input("How many options are there? "))
numberOfVoters = int(input("How many voters?"))

optionsList = [] 

for i in range (0, answersNr): 
    optionsList.append(input("Option number " + str(i+1) + "?\n"))
    print("")    

listFinal = []

for voter in range (0, numberOfVoters):
    listFinal.append([])
    input("\nPress enter to start voting.")
    print("\n\n ------------------")

    print(question)
    
    i = 1
    for option in optionsList: 
        print(str(i)+". " + option)
        i = i + 1 
    
    answer = input("What are your choices, ranked on your preference?\n") 
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for character in answer:
        if character in numbers:
            if int(character) > answersNr:
                pass
            elif character in listFinal[voter]:
                pass
            else:
                listFinal[voter].append(character)
            

print(listFinal)
