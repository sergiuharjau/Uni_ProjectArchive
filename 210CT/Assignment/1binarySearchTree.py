"""Build a Binary Search Tree (BST) to hold English language words in its nodes. Use a paragraph of
any text in order to extract words and to determine their frequencies.
Input: You should read the paragraph from a suitable file format, such as .txt. The following
tree operations should be implemented: a) Printing the tree in pre-order. b) Finding a word.
Regardless whether found or not found your program should output the path traversed in
determining the answer, followed by yes if found or no, respectively.
"""

class NodeTree():
    """Class that holds objects of nodes in a Binary Search Tree."""
    
    def __init__(self, data = None, parent = None, key = None):
        """Initalizes the first node, the root."""
        self.data = data 
        self.parent = parent #this is the parent node
        
        self.key = hash(data)
        
        self.right = None #holds node variable
        self.left = None 
        
    def insertInto(node, data):
        """Inserts element into subtree of node, following BST conventions."""
        if node.key == 625211: #First element
            node.data = data 
            node.key = hash(data)
        
        elif node.key > hash(data):
            if node.left == None:
                node.left = NodeTree(data, node)
            else:
                node.left.insertInto(data) #Try to insert at left child 
        else:
            if node.right == None:
                node.right = NodeTree(data, node)
            else:
                node.right.insertInto(data) #Try to insert at right child 

    def traversePreOrder(node):
        """Traverses tree in NLR manner."""
        dataList = [node.data] #Deals with the root being None
 
        if node.left != None:
            dataList += node.left.traversePreOrder()
        if node.right != None:
            dataList += node.right.traversePreOrder()
        return (dataList)
    
    def isElement(node, target, pathTraversed = []):
        """Returns a tuple of Yes/No + path traversed to the item."""
        pathTraversed += [node.key]    
        if node.data == target:
            return ("Yes" , pathTraversed)
        
        if hash(target) > node.key:
            if node.right == None:
                return("No", pathTraversed)
            else: 
                return node.right.isElement(target, pathTraversed)
        else:
            if node.left == None:
                return("No", pathTraversed)
            else: 
                return node.left.isElement(target, pathTraversed)
    
    def findElement(node, target):
        """Returns node object of target."""        
        if node.data == target:
            return node 
        
        if hash(target) > node.key:
            return node.right.findElement(target)
        else:
            return node.left.findElement(target)
    
    def printPreOder(node):
        """Prints NLR."""
        dataList = node.traversePreOrder()
        for element in dataList:
            print(element, end = " ")
            
    
if __name__ == "__main__":
    
    tree = NodeTree()
    
    while True:
        inputUser = input("Number to insert: ")
        if inputUser == ".":
            break
        else:
            tree.insertInto(int(inputUser))
    
    print(tree.findElement(6))