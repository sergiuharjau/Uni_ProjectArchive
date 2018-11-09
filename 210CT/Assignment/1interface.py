bst = __import__("1binarySearchTree")

intCheck = int(input("Are you inserting integers?\n1-yes\n0-no "))
print("\nWrite exit to stop.")
print("Write textfile to read from textfile.\n")
userInput = []
tree = bst.NodeTree() 
while True:
    element = input("Element: ")
    if element == "exit": break
    if element == "textfile": 
        for element in open("input.txt", "r").read().split(" "):
            tree.insertInto(element)
        break 
    else:
        if intCheck: 
            tree.insertInto(int(element))
        else: tree.insertInto(element)

while True:
    choice = int(input("1.Print in PreOrder(NLR)\n2.Find element\n3.Delete element\n4.Determine Frequency\n5.Exit\nChoice: "))
    
    if choice == 5:break
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
    elif choice == 4:
        print()
        for line in tree.determineFrequency():
            print(line)
        input()