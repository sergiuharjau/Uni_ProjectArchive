"""Implement the structure for an unweighted, undirected graph G, where nodes consist of
positive integers. Also, implement a function isPath(v, w), where v and w are vertices in the
graph, to check if there is a path between the two nodes. The path found will be printed to a
text file as a sequence of integer numbers (the node values).
Using the graph structure previously implemented, implement a function isConnected(G) to
check whether or not the graph is strongly connected. The output should be simply 'yes' or 'no'.
"""

class GraphStructure():
    """Unweighted, undirected graph class, positive integers as nodes."""
    
    def __init__(self, vertices, edges):
        
        self.adjacency = {} #nodes as keys, connections as lists
        
        for node in vertices:
            self.adjacency[node] = [] 
            for edge in edges:
                if node in edge:
                    if edge[0] != node:
                        self.adjacency[node].append(edge[0])
                    else: self.adjacency[node].append(edge[1])
    
    def isPath(self, start, target):
        """Returns True/False, followed by the path it took."""  
        if start not in self.adjacency or target not in self.adjacency:
            return False
        
        toVisit = [[start]]
        visited = [] 
        
        while toVisit != []:
            
            path = toVisit[0] 
            current = path[0] #current node will always be first in the path list
            
            if current in visited: 
                del toVisit[0] 
                continue
                
            if current == target:
                path.reverse() 
                return (True, path)        

            for i in range(len(self.adjacency[current])):
                toVisit.append( [ self.adjacency[current][i] ] + path )
                                        #appends adjacent node to toVisit + the path it took to it 
            visited.append(current)  
            del toVisit[0]
        
        return False  
    
    def isConnected(self):
        """Returns True/False, whether the graph is fully connected or not."""
        
        inGraph = []
        toVisit = [ list(self.adjacency.keys())[0] ] 
                            #first node 
        while toVisit != []:
            
            current = toVisit[0]      
            
            if current in inGraph:
                del toVisit[0]
                continue        
                
            toVisit += self.adjacency[current]         
            inGraph.append(current)
            del toVisit[0]
        
        for node in self.adjacency:
            if node not in inGraph:
                return False          
        return True