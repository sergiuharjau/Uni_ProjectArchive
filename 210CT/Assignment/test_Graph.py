import unittest 
gs = __import__("3graphStructure")

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        """Initiates a graph"""
        
        self.simpleG = gs.GraphStructure([1, 2, 3, 4, 5], [(1,2), (2,4), (3,4), (3,5), (4,5)])
        self.complexG = gs.GraphStructure([6, 7, 8, 9, 10, 11, 12, 13], [(6,7), (6,9), (6,8), (8,12), (12,9), (9,11), (9,10), (12,13)])
    
    def test_Creation(self):
        """Sanity check."""
        self.assertEqual(self.simpleG.getAdjacency(), {1: [2], 2: [1, 4], 3: [4, 5], 4: [2, 3, 5], 5: [3, 4]})
        self.assertEqual(self.complexG.getAdjacency(), {6: [7,9,8], 7: [6], 8: [6,12], 9:[6, 12, 11, 10], 10: [9], 11: [9], 12: [8, 9, 13], 13:[12]})
    def test_isPath(self):
        """Checks isPath() behaviour"""
        self.assertEqual(self.simpleG.isPath(3,4), [3, 4]) 
        self.assertEqual(self.simpleG.isPath(3,2), [3, 4, 2])
        self.assertEqual(self.simpleG.isPath(3,1), [3, 4, 2, 1])  
        self.assertEqual(self.simpleG.isPath(5,1), [5, 3, 4, 2, 1])
        self.assertEqual(self.simpleG.isPath(4,1), [4, 2, 1])
        
        self.assertEqual(self.complexG.isPath(9,7),  [9,6,7])
        self.assertEqual(self.complexG.isPath(10,7), [10,9,6,7])
        self.assertEqual(self.complexG.isPath(11,8), [11,9,6,8])
        self.assertEqual(self.complexG.isPath(8,13), [8,6,9,12,13])
        self.assertEqual(self.complexG.isPath(13,7), [13,12,8,6,7])
        
        
        self.assertEqual(self.simpleG.isPath(1,6), False) #not in graph
        self.assertEqual(self.simpleG.isPath(0,7), False)
        self.assertEqual(self.complexG.isPath(10, 100), False)
        self.assertEqual(self.complexG.isPath(1, 4), False)
        
        
        
if __name__ == "__main__":
    unittest.main() 