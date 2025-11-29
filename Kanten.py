from Knoten import coordinations


graph = {}


# In this function user will be asked to define the edges between nodes
def set_edges():
    global graph
    print("\t---------Your Nodes---------\n")
    for node in coordinations.keys():
        print("\t",node, end="  ")
    for node in coordinations:
        connections = input(f"\n \tFrom {node} to(e.g. : A B C ...): ").split()
        graph[node] = connections


# as the name says it will draw edges using the graph of connections which the user has set    
def draw_edges(t):
    global graph
    for key, val in graph.items():
        x, y = coordinations[key]
        t.penup()
        t.goto(x, y)
        
        for i in range(len(val)):
            t.pendown()
            x2, y2 = coordinations[val[i]]
            t.goto(x2,y2)
            t.goto(x,y)