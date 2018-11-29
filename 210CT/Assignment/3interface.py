gs = __import__("3graphStructure")

if input("Predetermined graph? ") != "yes":
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
else:
    graph = gs.GraphStructure([6, 7, 8, 9, 10, 11, 12, 13, 21, 24], [(6,7,2), (7,21,1), (21,24,1), (6,9,5), (6,8,2), (8,12,2), (12,9,3), (9,11,2), (9,10,2), (12,13,4)])   
    
while True:
    try: choice = int(input("\n1.isPath()\n2.isGraphConnected()\n3.BFS\n4.DFS\n5.Dijkstra\n6.Exit\nChoice: "))
    except: print("\n\nWe don't recognize your choice.\n"); continue
    try:
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
    except: print("Wrong input.")