import random
import math

colors = ["blue", "green", "purple", "orange", "red", "pink", "cyan"]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
coordinations = {}

r = 200

#Here user will set how many numbers he or she wants and the program creates the graph by itself
def set_number_of_nodes(t):
    
    number = int(input("How many nodes you wanna create : "))
    global r

    for i in range(number):
        angle_deg = (360 / number) * i
        angle_rad = math.radians(angle_deg)

        x = math.cos(angle_rad) * r
        y = math.sin(angle_rad) * r

        t.goto(x, y)
        t.dot(40, random.choice(colors))
        t.goto(x + 2, y - 8)
        t.write(alphabet[i], align="center", font=("Arial", 12, "bold"))

        coordinations[alphabet[i]] = [x, y]

#User will type the Names of the nodes like A B C and nodes will be set
def user_set_nodes(t):
    nodes = input("Give the names of the nodes as a list (e.g : A B C D ...)\n").split()

    number = len(nodes)
    global r

    for i in range(number):
        angle_deg = (360 / number) * i
        angle_rad = math.radians(angle_deg)

        x = math.cos(angle_rad) * r
        y = math.sin(angle_rad) * r

        t.goto(x, y)
        t.dot(40, random.choice(colors))
        t.goto(x + 2, y - 8)
        t.write(nodes[i], align="center", font=("Arial", 12, "bold"))

        coordinations[nodes[i]] = [x, y]
    
    
#User will be asked to be more exact and set the coordinations maually
def set_coordinations(t):
    
    number = int(input("How many nodes would you like to set: "))
    
    for i in range(number):
        raw = input(f"Set the {i}th coordination(e.g. x, y): ")
        a, b = raw.split(",")
        x, y = int(a), int(b)
        coordinations[alphabet[i]] = [x, y]

    for k, v in coordinations.items():
        x=(v[0])
        y=(v[1])
        
        t.goto(x,y)
        t.dot(40, random.choice(colors))
        t.goto(x + 2, y - 8)
        t.write(k, align="center", font=("Arial", 12, "bold"))