bst = __import__("1binarySearchTree")

print("Be advised. Write exit to stop.")
userInput = []
tree = bst.NodeTree() 
intCheck = int(input("Are you inserting integers? 1-yes "))
while True:
    element = input("Element: ")
    if element == "exit": break
    else:
        if intCheck: 
            tree.insertInto(int(element))
        else: tree.insertInto(element)

while True:
    choice = int(input("1.Print in PreOrder(NLR)\n2.Find element\n3.Delete element\n4.Exit\nChoice: "))
    
    if choice == 4:break
    elif choice == 1:
        print("\nCurrent Binary Tree in PreOrder: ")
        tree.printPreOrder() 
        input()
    elif choice == 2: 
        element = input("\nWhich element? ")
        if intCheck:
            results = tree.isElement(int(element))
        else: results = tree.isElement(element)
        print("In the tree? ", end = "")
        print(results[-1] + "\nPath: ", end = "")
        for i in range(len(results)-1): print(results[i], end=" ")
        print()
        input()
    elif choice == 3: 
        element = input("\nWhich element? ")
        if intCheck:
            tree.deleteNode(int(element))
        else: tree.deleteNode(element)
        print("Element deleted.")
        input() 