import Knoten
import turtle
import Kanten
import DFS


def main():   
    gerichtet=False

    print("a)die anzahl von knoten")
    print("b)die Namen von knoten")
    print("c)die koordinaten von knoten")
    eingabe=input("choose\n")

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()


    match eingabe:

        case "a":
            Knoten.self_nodes(t)
            
        case "b":
            Knoten.user_nodes(t)

        case "c":
            Knoten.koordinaten_knoten(t)
        case _:
            print("ridi")
            
    graph = Kanten.create_kanten(t)
    Kanten.draw_kanten(graph, t)
    


    choice=input("graph gezeichnet wählen Sir zwichen bfs oder baum\n")
    DFS.dfs(graph,t)
    turtle.done()


if __name__ == "__main__":
    main()