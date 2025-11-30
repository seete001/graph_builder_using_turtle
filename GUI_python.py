import tkinter as tk
import turtle
import tkinter.simpledialog as sd
import tkinter.messagebox as mb



# ==== IMPORT YOUR MODULES ====
import Knoten
import Kanten
import GraphDfs

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ============================================================
#  Create main Tkinter window
# ============================================================
root = tk.Tk()
root.title("Graph Builder using Turtle")
root.geometry("900x600")


# ============================================================
# Embed a Turtle screen inside Tkinter
# ============================================================
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack(side=tk.RIGHT)

turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("white")

t = turtle.RawTurtle(turtle_screen)
t.hideturtle()
t.penup()


# ============================================================
#  FUNCTIONS used by buttons
# ============================================================


def set_nodes():
    num = sd.askinteger("Number of Nodes", "Enter number of nodes:")
    if num is None:
        return  
    Knoten.set_number_of_nodes(num, t)


def set_node_names():
    raw = sd.askstring(
        "Node Names",
        "Give the names of the nodes as a list (e.g: A B C D ...):"
    )

    if not raw:
        print("No names entered or cancelled.")
        return

    names = raw.split()

    Knoten.user_set_nodes(names, t)


def set_coordinates():
    Knoten.coordinations = {}
    number = sd.askinteger("Set coordinations yourserlf format:x, y", "How many numbers do you have")


    for i in range(number):
        name = alphabet[i]

        raw = sd.askstring(
            "Set coordinates",
            f"Enter coordinates for node '{name}' (format: x,y):"
        )
        x, y = raw.split(",")

        Knoten.coordinations[name] = [float(x), float(y)]
        print(Knoten.coordinations)

    Knoten.set_coordinations(t)


graph = {}

def set_edges():
    global graph
    graph = {}

    nodes = list(Knoten.coordinations.keys())

    if not nodes:
        print("No nodes exist yet!")
        return

    for node in nodes:
        raw = sd.askstring(
            f"Connections for {node}",
            f"Nodes available: {nodes}\n\n"
            f"Enter neighbors of {node} (e.g. A B C):"
        )

        if raw is None:
            print("Cancelled.")
            return

        # Split input into list
        parts = raw.upper().replace(",", " ").split()

        # Keep only valid nodes
        connections = [p for p in parts if p in nodes and p != node]

        graph[node] = connections

    print("Graph set:", graph)

def draw_edges_button():
    Kanten.draw_edges(graph, t)

def check_tree():
    if not graph:
        mb.showinfo("DFS Result", "Graph is empty!")
        return

    is_tree, message = GraphDfs.dfs(graph)
    if is_tree:
        mb.showinfo("DFS Result", f"Yes! The graph is a tree.\n{message}")
    else:
        mb.showwarning("DFS Result", f"No! The graph is not a tree.\n{message}")


def clear_canvas():
    t.clear()


# ============================================================
#  GUI LAYOUT — LEFT SIDE BUTTON PANEL
# ============================================================

label = tk.Label(root, text="Choose how to build your Graph:",
                 font=("Arial", 14))
label.pack(pady=20, padx=20, anchor="nw")

buttons_frame = tk.Frame(root)
buttons_frame.pack(side=tk.LEFT, padx=20, anchor="n")


def make_button(text, command):
    btn = tk.Button(buttons_frame, text=text, command=command,
                    font=("Arial", 12), width=22, height=2)
    btn.pack(pady=6)
    return btn


make_button("Set number of nodes", set_nodes)
make_button("Set node names", set_node_names)
make_button("Set coordinates", set_coordinates)
make_button("Set edges", set_edges)
make_button("Draw edges", draw_edges_button)
make_button("Check if graph is a tree", check_tree)
make_button("Clear drawing", clear_canvas)

exit_btn = make_button("Exit", root.destroy)


# ============================================================
#  Start GUI
# ============================================================
root.mainloop()
