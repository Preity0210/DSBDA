graph = {
    'A': {'B':1, 'C':4},
    'B': {'C':2},
    'C': {}
}

dist = {'A':0, 'B':999, 'C':999}

for node in graph:
    for nbr in graph[node]:
        dist[nbr] = min(dist[nbr], dist[node] + graph[node][nbr])

print(dist)