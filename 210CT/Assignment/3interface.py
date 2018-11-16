gs = __import__("3graphStructure")

print("\nLeave blank to stop.")
vertices = [] 
while True:
    node = input("Vertice: ") 
    if node == "":
        break
    else: vertices.append(int(node))
        
print("\nPlease provide adjacent nodes for these vertices. Once for every connection.")
edgePairs = [] 

for node in vertices:    
    print(str(node) + ": ", end=" ")
    edge = input()
    for element in edge.split(","):
        if element != "":
            edgePairs.append((int(element),node,0))

graph = gs.GraphStructure(vertices, edgePairs)

while True:
    try: choice = int(input("\n1.isPath()\n2.isGraphConnected()\n3.BFS\n4.DFS\n5.Dijkstra\n6.Exit\nChoice: "))
    except: print("\n\nWe don't recognize your choice.\n"); continue
    
    if choice == 6:break 
    elif choice == 1:
        userInput = input("\nGive two vertices as such: x,y\n").split(",")
        result = graph.isPath(int(userInput[0]), int(userInput[1]))
        print("\nAre they connected? " + str(result[0]))
        if len(result) > 1:
            print("Path: " + str(result[1]))
        input()
    elif choice == 2:   
        print("\nIs the graph connected?")
        print(graph.isConnected())
        input()
    elif choice == 3:
        node = int(input("\nAt which node do you want to start? "))
        print("This is Breadth First Traversal: ")
        print(graph.traverseBreadthFirst(node))
        input()
    elif choice == 4:
        node = int(input("\nAt which node do you want to start? "))
        print("This is Depth First Traversal:")
        print(graph.traverseDepthFirst(node))
        input()
    elif choice ==5:
        userInput = input("\nGive two vertices as such: x,y\n").split(",")
        result = graph.findDijkstra(int(userInput[0]), int(userInput[1]))
        print("This is the path: " + str(result)) 
        input()    