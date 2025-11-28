


def dfs(graph,t):
    
    seen = set()
    nodes = list(graph.keys())
    if not nodes:
        return False
    stack = [[nodes[0], None]]
    while stack:
        node, parent = stack.pop()
        if node in seen:
            print("Cycle")
            return False, "Graph has a Cycle"
        seen.add(node)

        for neigh in graph[node]:
            if neigh != parent:
                stack.append([neigh, node])

    if seen != set(graph.keys()):
        missing = set(graph.keys()) - seen 
        print("Missing")
        return False, f"These Nodes are not connected{missing}"        
    return True, "Graph is Tree"