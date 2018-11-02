import unittest 
bst = __import__("1binarySearchTree")

class TestBST(unittest.TestCase):
    
    def setUp(self):
        """Initiates two binary search trees, to be used during testing."""
        bigTest = [10, 15, 20, 13, 0, 5, 7, 3, -2, -1, 25, 18, 14, 12]
        smallTest = [5, 3, 8, 1, 4, 6, 12]
        
        self.bigTree = bst.NodeTree() 
        self.smallTree = bst.NodeTree() 
        
        for element in bigTest:
            self.bigTree.insertInto(element)
        
        for element in smallTest:
            self.smallTree.insertInto(element)
        
    def test_insertion(self):
        """Checks if insertion behaves correctly, on two separate trees."""
        smallResult = [5,3,1,4,8,6,12] 
        bigResult = [10, 0, -2, -1, 5, 3, 7, 15, 13, 12, 14, 20, 18, 25]
        
        i = 0 
        for element in self.smallTree.traversePreOrder():
            self.assertEqual(element, smallResult[i])
            i+=1 
        i=0 
        for element in self.bigTree.traversePreOrder():
            self.assertEqual(element, bigResult[i])
            i+=1 
    
    def test_parentalChecking(self):
        """Checks if parent/ child lookup behaves normally"""
            
        kids    = [13, 5, 3, -2, 25] 
        parents = [15, 0, 5,  0, 20]

        for i in range(len(kids)):
            for j in range(len(parents)):
                if i==j:
                    self.assertEqual(self.bigTree.fetchNode(kids[i]).parent.data , parents[i])
            
    def test_isWord(self):
        
        self.assertEqual(self.bigTree.isElement(12), ("Yes", [10, 15, 13, 12]))
        
        self.assertEqual(self.bigTree.isElement(5), ("Yes", [10, 0, 5])) 
    
    
    def test_fetchWordNode(self):
        
        self.assertEqual(self.bigTree.fetchNode(12).data, 12)
        self.assertEqual(self.bigTree.fetchNode(100).data, None) 
        
    
    def test_preOrder(self):
        
        smallResult = [5,3,1,4,8,6,12]
        bigResult = [10, 0, -2, -1, 5, 3, 7, 15, 13, 12, 14, 20, 18, 25]
        
        self.assertEqual(self.smallTree.traversePreOrder(), smallResult)
        self.assertEqual(self.bigTree.traversePreOrder(), bigResult)
    
    
    
    def test_deletion(self):
        pass
        
if __name__ == "__main__":
    unittest.main() 