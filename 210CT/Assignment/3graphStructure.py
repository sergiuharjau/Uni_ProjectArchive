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
        self.exclusions = [] 
        
        for node in vertices:
            self.adjacency[node] = [] 
            for edge in edges:
                if node in edge:
                    if edge[0] != node:
                        self.adjacency[node].append(edge[0])
                    else: self.adjacency[node].append(edge[1])
    
    def isPath(self, v, w):
        """Returns path from v to w, if it exists."""
        if v not in self.adjacency or w not in self.adjacency:
            return False
        path = [v] 
        if w in self.adjacency[v]:
            path += [w]
        else:
            for node in self.adjacency[v]:
                if self.adjacency[node] == [v]: #if node we want to go to is leaf, skip it
                    pass
                elif node not in self.exclusions:
                    self.exclusions.append(node) #makes sure we never backtrack
                    path += self.isPath(node,w)
                if w in path: break
                    
        self.exclusions = [] #reset exclusions      
        return path
    
    def getAdjacency(self):
        """Returns adjacency dictionary"""
        return self.adjacency
            