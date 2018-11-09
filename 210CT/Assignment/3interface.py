gs = __import__("3graphStructure")

print("\nWrite exit to stop.")
vertices = [] 
while True:
    node = input("Vertice: ")
    
    if node == "exit":
        break
    else: vertices.append(int(node))
        
print("\nPlease provide adjacent nodes for these vertices.")
edgePairs = [] 

for node in vertices:    
    print(str(node) + ": ", end=" ")
    edge = input()
    for element in edge.split(","):
        if element != "":
            edgePairs.append((int(element),node))

print(edgePairs)        

graph = gs.GraphStructure(vertices, edgePairs)

print(graph.getAdjacency())

while True:
    userInput = input("").split(",")
    
    print(graph.isPath(int(userInput[0]), int(userInput[1])))
    