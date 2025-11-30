import Knoten
import turtle
import Kanten
import GraphDfs

t = turtle.Turtle()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():   
    directed = False
    
    print("\033[2J\033[H")
    print("1. Set number of nodes")
    print("2. Set the names of nodes")
    print("3. Set the coordinations")
    print("4. Exit")
    choice = int(input("choose: "))

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    nodes = []
    match choice:

        case 1:
            number = int(input("How many nodes you got: "))
            Knoten.set_number_of_nodes(number, t)
        case 2:
            nodes = input("Enter the names (format: A B C ..): ").split()
            Knoten.user_set_nodes(nodes, t)
        case 3:
            Knoten.coordinations = {}
            n = int(input("How many nodes you got: "))
            for i in range(n):
                raw = input("Enter the {i + 1}th coordination(format: x, y): ")
                a,b = raw.split(",")
                lst = [float(a), float(b)]
                Knoten.coordinations[alphabet[i]] = lst
            Knoten.set_coordinations(t)
        case 4:
            exit()
            
    graph = {}
    for node in nodes:
        connections = input(f"Enter the neighbours of {node}: ").split()
        graph[node] = connections


    Kanten.draw_edges(graph, t)
    
    isTree = GraphDfs.dfs(graph)

    if not isTree[0]:
        print("This is not a Tree", isTree[1])
    else:
        print("It can be a Tree")
    
    turtle.done()


if __name__ == "__main__":
    main()