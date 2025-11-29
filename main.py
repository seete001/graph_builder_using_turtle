import Knoten
import turtle
import Kanten
import DFS


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


    match choice:

        case 1:
            Knoten.set_number_of_nodes(t)
        case 2:
            Knoten.user_set_nodes(t)
        case 3:
            Knoten.set_coordinations(t)
        case 4:
            exit()
            
    Kanten.set_edges()

    Kanten.draw_edges(t)
    
    isTree = DFS.dfs()

    if not isTree[0]:
        print("This is not a Tree", isTree[1])
    else:
        print("It can be a Tree")
    
    turtle.done()


if __name__ == "__main__":
    main()