import Knoten


# as the name says it will draw edges using the graph of connections which the user has set    
def draw_edges(graph, t):
    print(graph)

    for a, neighbors in graph.items():

        x1, y1 = Knoten.coordinations[a]
        
        for neighbour in neighbors:
            x2, y2 = Knoten.coordinations[neighbour]
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)
            t.penup()

            
