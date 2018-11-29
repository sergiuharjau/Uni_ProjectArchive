import unittest 
gs = __import__("3graphStructure")

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        """Initiates a graph"""                               #(node, node, weight) 
        self.simpleG = gs.GraphStructure([1, 2, 3, 4, 5], [(1,2,3), (2,4,3), (3,4,5), (3,5,1), (4,5,2)])
        self.complexG = gs.GraphStructure([6, 7, 8, 9, 10, 11, 12, 13, 21, 24], [(6,7,2), (7,21,1), (21,24,1), (6,9,5), (6,8,2), (8,12,2), (12,9,3), (9,11,2), (9,10,2), (12,13,4)])   
        self.brokenGraph = gs.GraphStructure([1,2,3,4], [(1,2,0), (2,3,0)])
        
    def test_Creation(self):
        """Sanity check."""
        self.assertEqual(self.simpleG.adjacency, {1: [ (2,3) ], 2: [ (1,3), (4,3) ], 3: [ (4,5) , (5,1) ], 4: [ (2,3), (3,5), (5,2) ], 5: [ (3,1), (4,2) ]})
        self.assertEqual(self.complexG.adjacency, {6: [ (7,2) , (9,5) , (8,2) ], 7: [ (6,2) , (21,1) ], 8: [ (6,2) , (12,2) ], 9:[ (6,5), (12,3), (11,2), (10,2) ], 10: [(9,2)], 11: [(9,2)], 12: [(8,2), (9,3), (13,4)], 13:[(12,4)], 21:[(7,1), (24,1)], 24:[(21,1)]})
    
    def test_Updating(self):
        """Tests behaviour of addNode, addEdges, deleteNode, and deleteEdges"""
        self.simpleG.addNode(6, [(4,2),(1,1)]) #Simple insertion check 
        self.assertEqual(self.simpleG.adjacency, {1: [ (2,3), (6,1) ], 2: [ (1,3), (4,3) ], 3: [ (4,5) , (5,1) ], 4: [ (2,3), (3,5), (5,2), (6,2) ], 5: [ (3,1), (4,2)], 6:[(4,2), (1,1)]})
        self.assertEqual(self.simpleG.traverseDepthFirst(1), [1,2,4,3,5,6]) #checks functions can still traverse tree
    
        self.simpleG.addEdges( [(2,6,1) , (2,3,2)] ) #Edge addition check
        self.assertEqual(self.simpleG.adjacency, {1: [ (2,3), (6,1) ], 2: [ (1,3), (4,3), (6,1), (3,2) ], 3: [ (4,5) , (5,1), (2,2) ], 4: [ (2,3), (3,5), (5,2), (6,2) ], 5: [ (3,1), (4,2)], 6:[(4,2), (1,1), (2,1)]})
        self.assertEqual(self.simpleG.traverseDepthFirst(6), [6, 4, 2, 1, 3, 5])
        
        self.simpleG.deleteNode(6)
        self.assertEqual(self.simpleG.adjacency, {1: [ (2,3) ], 2: [ (1,3), (4,3), (3,2) ], 3: [ (4,5) , (5,1), (2,2) ], 4: [ (2,3), (3,5), (5,2), ], 5: [ (3,1), (4,2) ] })
        
        self.simpleG.deleteEdges( [(2,3)] )
        self.assertEqual(self.simpleG.adjacency, {1: [ (2,3) ], 2: [ (1,3), (4,3) ], 3: [ (4,5) , (5,1) ], 4: [ (2,3), (3,5), (5,2) ], 5: [ (3,1), (4,2) ]})
        
    def test_isPath(self):
        """Checks isPath() behaviour"""
        self.assertEqual(self.simpleG.isPath(3,4), (True, [3, 4]))
        self.assertEqual(self.simpleG.isPath(3,2), (True, [3, 4, 2]))
        self.assertEqual(self.simpleG.isPath(3,1), (True, [3, 4, 2, 1]) ) 
        self.assertEqual(self.simpleG.isPath(5,1), (True, [5, 4, 2, 1]))
        self.assertEqual(self.simpleG.isPath(4,1), (True, [4, 2, 1]))
        
        self.assertEqual(self.complexG.isPath(9,7),  (True, [9,6,7]))
        self.assertEqual(self.complexG.isPath(10,7), (True, [10,9,6,7]))
        self.assertEqual(self.complexG.isPath(11,8), (True, [11,9,6,8]))
        self.assertEqual(self.complexG.isPath(8,13), (True, [8,12,13]))
        self.assertEqual(self.complexG.isPath(13,7), (True, [13,12,8,6,7]))
     
        
        self.assertEqual(self.simpleG.isPath(1,6), [False]) #not in graph
        self.assertEqual(self.simpleG.isPath(0,7), [False])
        self.assertEqual(self.complexG.isPath(10, 100), [False])
        self.assertEqual(self.complexG.isPath(1, 4), [False])
   
    def test_isConnected(self):
        """Checks isConnected() behaviour."""
        
        self.assertEqual(self.simpleG.isConnected(), True)
        self.assertEqual(self.complexG.isConnected(), True)
        self.assertEqual(self.brokenGraph.isConnected(), False)
        
    def test_breadthFirst(self):
        """Checks traverseBreadthFirst() behaviour."""
        
        self.assertEqual(self.simpleG.traverseBreadthFirst(4), [4, 2, 3, 5, 1])
        self.assertEqual(self.complexG.traverseBreadthFirst(9), [9, 6, 12, 11, 10, 7, 8, 13, 21, 24])
        self.assertEqual(self.brokenGraph.traverseBreadthFirst(2), [2,1,3,4]) 
        self.assertEqual(self.brokenGraph.traverseBreadthFirst(4), [4,1,2,3])
    
    def test_depthFirst(self):
        """Checks traverseDepthFirst() behaviour."""
        
        self.assertEqual(self.complexG.traverseDepthFirst(9), [9, 6, 7, 21, 24, 8, 12, 13, 11, 10])
        self.assertEqual(self.complexG.traverseDepthFirst(11), [11, 9, 6, 7, 21, 24, 8, 12, 13, 10]) 
        self.assertEqual(self.complexG.traverseDepthFirst(8), [8, 6, 7, 21, 24, 9, 12, 13, 11, 10])
            #can only be really seen on big graphs
    
    def test_dijkstra(self):
        """Checks dijkstra algorithm functionality."""
        
        self.assertEqual(self.simpleG.findDijkstra(1,5), [1,2,4,5])
        self.assertEqual(self.complexG.findDijkstra(13,6), [13, 12, 8, 6])
        self.assertEqual(self.complexG.findDijkstra(11,6), [11, 9, 6])
        
        self.assertEqual(self.complexG.findDijkstra(11,0), [None]) #not in graph 
    
if __name__ == "__main__":
    unittest.main() 