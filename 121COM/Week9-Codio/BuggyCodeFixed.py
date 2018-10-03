class ToDoList:
    def __init__(self, startList=[]):
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
        if num > len(self.theList):
            pass
        else: 
            self.crossed.append(num-1)

if __name__ == "__main__":
    shoppingList = ToDoList(["Test1", "Test2"])
    shoppingList.addToList("Milk")
    shoppingList.addToList("Bread")
    shoppingList.addToList("Eggs")
    shoppingList.addToList("Flowers")
    shoppingList.addToList("Hat")   
    shoppingList.addToList("Something new")
    shoppingList.readList()
    shoppingList.crossOfList(9)
    shoppingList.crossOfList(2)
    shoppingList.crossOfList(6)    
    shoppingList.readList()    
    shoppingList.addToList("9th element")
    
    shoppingList.readList()
    
    
# You can cross off elements which don't exist, and then when you add new elements,
#they get crossed off upon reading 
# To fix this, we need to make sure the user can only cross off existing elements

