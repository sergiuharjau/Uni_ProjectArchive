class ToDoList:
    
    def __init__(self, startList=None):
        if startList == None: 
            startList = [] 
        else:
            pass
        self.theList = startList
        self.crossed = []

    def readList(self):
        print("----------")
        count=1
        for i in range(len(self.theList)):
            if i in self.crossed:
                print(str(count) + ". |x| " + self.theList[i])
            else:
                print(str(count) + ". | | " + self.theList[i])
            count=count+1
        print("----------")
        
    def addToList(self, newString):
        self.theList.append(newString)
        
    def crossOfList(self, num):
        self.crossed.append(num-1)

if __name__ == "__main__":
    shoppingList = ToDoList()
    shoppingList.addToList("Test 1")
    shoppingList.readList()
    print("First list" + str(shoppingList.theList))
    
    shoppingList2 = ToDoList()

    print("Second list" + str(shoppingList.theList))
    shoppingList2.addToList("Test Thing")
    shoppingList2.readList()
    
