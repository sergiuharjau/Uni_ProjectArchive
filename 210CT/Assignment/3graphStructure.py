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
        """Vertices as list, edges as list of tuples"""
        self.adjacency = {} #nodes as keys, connections as lists

        for node in vertices:
            self.adjacency[node] = [] 
            for edge in edges:
                if node in edge: 
                    if edge[1] == node:
                        self.adjacency[node].append( (edge[0], edge[2])   )
                    elif edge[0] == node: 
                        self.adjacency[node].append( edge[1:3] )
                                                    #tuple of (node,weight) 
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
                toVisit.append( [ self.adjacency[current][i][0] ] + path )
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
                
            for element in self.adjacency[current]:
                toVisit.append(element[0])  
                
            inGraph.append(current)
            del toVisit[0]
        
        for node in self.adjacency:
            if node not in inGraph:
                return False          
        return True
    
    def traverseBreadthFirst(self, toStart):
        """Returns sequence of nodes in breadth first manner."""
        
        toVisit = [toStart]
        visited = [] 
        
        while toVisit != []:
            
            current = toVisit[0]
     
            if current in visited:
                del toVisit[0]
                continue
            
            for node in self.adjacency[current]:
                if node not in visited:
                    toVisit.append(node[0])
                    
            visited.append(current)
            del toVisit[0]
       
        
        for node in self.adjacency:
            if node not in visited:
                visited.append(node)

        return (visited)
    
    def traverseDepthFirst(self, toStart, visited=[]):
        """Recursively returns sequence of nodes in depth first manner."""
        count = 0
        for node in self.adjacency[toStart]: #base case
            if node in visited:
                count += 1 
        if count == len(self.adjacency[toStart]):
            return visited #if all neighbours have been visited, nothing to do
        
        if visited == []: #first function call
            visited = [toStart]      
                
        for node in self.adjacency[toStart]: #for all neighbours
            if node[0] not in visited:
                visited.append(node[0])
                visited = self.traverseDepthFirst(node[0], visited)
            
        return visited
            
    def findDijkstra(self, toStart, end):
        """Finds shortest path between to vertices of a given Graph using Dijkstra."""
      
        if toStart not in self.adjacency or end not in self.adjacency:
            return None
        
        current = toStart
        
        nodesProp = {} 
        for node in self.adjacency:
            nodesProp[node] = {"edges": self.adjacency[node], "dist" : None , "prev" : None}
       
        nodesProp[toStart]["dist"] = 0 
        visited = [] 
        
        while current != end:     
            for neighbour in self.adjacency[current]:
                newDist = nodesProp[current]["dist"] + neighbour[1] #weight 
                if nodesProp[neighbour[0]]["dist"] == None or newDist < nodesProp[neighbour[0]]["dist"]:
                    nodesProp[neighbour[0]]["dist"] = newDist
                    nodesProp[neighbour[0]]["prev"] = current 
            
            visited.append(current)
            
            minimum = None
            for node in nodesProp: #finds minimum distance
                if nodesProp[node]["dist"] == None:
                    continue 
                if minimum == None or nodesProp[node]["dist"] < nodesProp[minimum]["dist"]:
                    if node not in visited:
                        minimum = node 
                        
            current = minimum #next to look at 
        
        path = [end]
        while True:
            path.append(nodesProp[end]["prev"])
            end = nodesProp[end]["prev"]
            if end == toStart:
                break
        path.reverse()
        return path
        
        
        
        
        
        
        
        
        