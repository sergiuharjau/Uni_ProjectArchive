import pickle 

f = open("words.txt", "r")
oneGiantString = f.read()
f.close()

wordList = oneGiantString.split("\n")


f= open("PickledWordList.pkl","wb")
pickle.dump(wordList,f)
f.close()