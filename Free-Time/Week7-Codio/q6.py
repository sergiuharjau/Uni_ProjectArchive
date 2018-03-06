import random

def createAI(filename):
    
    f1=open(filename, "r")
    bigString=f1.read()
    f1.close()
    wordsList=[]
    
    linesList=bigString.split("\n")
    for line in linesList:
        wordsPerLineList=line.split()
        for word in wordsPerLineList:
            wordsList.append(word)
    
    for word in wordsList:
        if word == word.upper():
            wordsList.remove(word)
            
    dictionary = {}
    
    position = -1
    while position < len(wordsList) -2 :
        position += 1
        if wordsList[position] in dictionary:
            dictionary[wordsList[position]].append(wordsList[position+1])
        else:
            dictionary[wordsList[position]] = [wordsList[position+1]]
            
    x = random.randint(0,len(wordsList))
    fullStopCheck=0
    i=-1
    
    print("Beware! It speaks!\n")
    
    while fullStopCheck==0:
        i+=1
        if i==0:
            listUpper=[]
            while listUpper==[]:
                list1 = dictionary[wordsList[x]]
                x = random.randint(0,len(list1)-1)
                word = list1[x]
                if word[0].isupper():
                    listUpper.append(word)
                
            print(word, end=" ")
        else:
            list2 = dictionary[word]
            x = random.randint(0,len(list2)-1)
            word = list2[x]
            if word[0].isupper():
                continue
            if word[len(word)-1] == "!" or word[len(word)-1] == "?":
                fullStopCheck=1
            if word[len(word)-1] == "." and i>30:
                if word=="Mr.":
                    pass
                else:
                    fullStopCheck=1
            print(word, end=" ")
    print("\n\nOh. That was disappointing.")
    return(dictionary)

dictionary=createAI("Book.txt")

        
    