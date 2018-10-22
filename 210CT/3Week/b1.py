def readWords(n):
    """Read n words separated by spaces from input."""
    userInput = input("Please type " + str(n) + " words separated by spaces:\n")
    words = [] 
    startIndex = 0 
    for i in range(len(userInput)):
        if userInput[i] == " ":
            words.append(userInput[startIndex:i])
            startIndex = i + 1
    if userInput[startIndex:len(userInput)] not in words: 
        words.append(userInput[startIndex:len(userInput)])
    
    while " " in words:
        words.remove(" ")
        
    return words[:4]

def mirror(word):
    
    result = ""
    
    for i in reversed(range(len(word))):
        result += word[i]

    return result 

def mirrorList(wordList):
    
    result = [] 
    
    for element in wordList: 
        result.append(mirror(element))
        
    return result 
    
if __name__ == "__main__":
    
    n = input("Number of words: ")
    words = readWords(n)
    
    newWords = mirrorList(words)
    
    for element in newWords:
        print(element, end = " ")
    
    print()
    