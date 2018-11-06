"""Build a Binary Search Tree (BST) to hold English language words in its nodes. Use a paragraph of
any text in order to extract words and to determine their frequencies.
Input: You should read the paragraph from a suitable file format, such as .txt. The following
tree operations should be implemented: a) Printing the tree in pre-order. b) Finding a word.
Regardless whether found or not found your program should output the path traversed in
determining the answer, followed by yes if found or no, respectively.
"""

class NodeTree():
    """Class that holds objects of nodes in a Binary Search Tree."""
    
    def __init__(self, data = None, parent = None):
        """Initalizes the first node, the root."""
        self.data = data 
        self.parent = parent #this is the parent node    
        self.right = None #will hold node variable in the future
        self.left = None 
        
    def insertInto(node, data):
        """Inserts element into subtree of node, following BST conventions."""
        if node.data == None: #First insertion 
            node.data = data 
        elif node.data > data:
            if node.left == None: #If empty, populates
                node.left = NodeTree(data, node)
            else:
                node.left.insertInto(data) #Try to insert at left child 
        else:
            if node.right == None:
                node.right = NodeTree(data, node)
            else:
                node.right.insertInto(data) #Try to insert at right child 
    
    def isElement(node, target):
        """Returns a tuple of Yes/No + path traversed to the item."""
        if node.data == target:
            return([node.data, "Yes"])

        pathTraversed = [node.data]  
        
        if target > node.data:
            if node.right == None: 
                return([node.data, "No"])
            else:
                pathTraversed += node.right.isElement(target) 
        else:                   #looks in the appropriate direction
            if node.left == None:
                return([node.data, "No"])
            else:
                pathTraversed += node.left.isElement(target)

        return pathTraversed
    
    def fetchNode(node, target):
        """Returns node object of target. Returns empty node if target not in tree."""        
        if node.data == target:
            return node 
        
        if target > node.data:
            if node.right != None:
                return node.right.fetchNode(target)
        else:
            if node.left != None:
                return node.left.fetchNode(target)
        
        return NodeTree()  #empty node 

    def traversePreOrder(node):
        """Traverses tree in NLR manner."""
        dataList = [node.data] #Will show the value of the nodes.
 
        if node.left != None:
            dataList += node.left.traversePreOrder()
        if node.right != None:
            dataList += node.right.traversePreOrder()
            
        return (dataList)
    
    def printPreOrder(node):
        """Prints NLR."""
        dataList = node.traversePreOrder()
        for element in dataList:
            print(element, end = " ")
        print() 
    
    def findLowest(node):
        """Returns the lowest value from  the right of a given node."""
        newRoot = node.right 
        minimum = newRoot.data
        while newRoot != None:
            if minimum > newRoot.data:
                minimum = newRoot.data 
            newRoot = newRoot.left 
        return minimum      

    def deleteNode(root, value): 
        """Deletes node of value in tree starting root."""
        nodeTBD = root.fetchNode(value)
            #To Be Deleted 
        if nodeTBD.parent == None: #If we're deleting root  
            nodeTBD.data = None  
        elif nodeTBD.isLeaf():
            if nodeTBD.parent.left == nodeTBD:
                nodeTBD.parent.left = None 
            else:
                nodeTBD.parent.right = None 
        #2 children 
        elif nodeTBD.right != None and nodeTBD.left !=None:
            nodeToSwap = nodeTBD.fetchNode(nodeTBD.findLowest())
            nodeTBD.data = nodeToSwap.data #transfer data over 
            if nodeToSwap.parent.left == nodeToSwap:
                nodeToSwap.parent.left = None #delete swapped node 
            else:
                nodeToSwap.parent.right = None                 
        else: #1 child
            if nodeTBD.left != None: #left branch 
                if nodeTBD.parent.left == nodeTBD: 
                    nodeTBD.parent.left = nodeTBD.left 
                else:
                    nodeTBD.parent.right = nodeTBD.left 
            else: #right branch 
                if nodeTBD.parent.left == nodeTBD:
                    nodeTBD.parent.left = nodeTBD.right 
                else:
                    nodeTBD.parent.right = nodeTBD.right

    def isLeaf(node):
        """Returns bool whether node is leaf or not."""
        if node.right == None and node.left == None:
            return True
        else:
            return False 
        
if __name__ == "__main__":
    pass