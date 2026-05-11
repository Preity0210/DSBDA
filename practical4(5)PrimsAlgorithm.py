graph = {
    'A': {'B':1, 'C':4},
    'B': {'A':1, 'C':2},
    'C': {'A':4, 'B':2}
}

visited = ['A']

while len(visited) < len(graph):

    minEdge = None

    for v in visited:
        for nbr in graph[v]:

            if nbr not in visited:

                if minEdge is None or graph[v][nbr] < minEdge[2]:
                    minEdge = (v, nbr, graph[v][nbr])

    print(minEdge[0], "-", minEdge[1], "=", minEdge[2])

    visited.append(minEdge[1])