import pickle

def anagram(filenamePickled,numberOfLetters):
    dictionary={}
    check=1
    f1=open(filenamePickled,"rb")
    wordList= pickle.load(f1)
    for word in wordList:
        if len(word)!=numberOfLetters:
            continue
        interList=list(word)
        interList.sort()
        key=tuple(interList)
        if key in dictionary:
            dictionary[key]+=1
        else:
            dictionary[key]=1
    for key in dictionary:
        if dictionary[key] <= check:
            pass
        else:
            check=dictionary[key]
    for key in dictionary:
        if dictionary[key] == check:
            print("Letters:" + str(numberOfLetters) + " Anagrams:" + str(check) ,key)
    return(dictionary)

for i in range (1,27):
    anagram("PickledWordList.pkl",i)