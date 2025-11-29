from Kanten import graph

#Depth first Search to search for a Cycle or missing nodes to validate whether it is a tree or not
def dfs():

    global graph
    
    seen = set()
    
    nodes = list(graph.keys())
    
    if not nodes:
    
        return False, "This is not a Graph"
    
    stack = [[nodes[0], None]]
    
    while stack:
    
        node, parent = stack.pop()
    
        if node in seen:

            return False, "Graph has a Cycle"
    
        seen.add(node)
    
        for neigh in graph[node]:
        
            if neigh != parent:
        
                stack.append([neigh, node])

    if seen != set(graph.keys()):
    
        missing = set(graph.keys()) - seen 
    
        return False, f"These Nodes are not connected{missing}"        
    
    return True, "Graph is Tree"