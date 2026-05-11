def safe(node, color, graph, c):

    for i in range(len(graph)):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True


def solve(node, graph, m, color):

    if node == len(graph):
        print("Coloring:", color)
        return True

    for c in range(1, m+1):

        if safe(node, color, graph, c):
            color[node] = c

            if solve(node+1, graph, m, color):
                return True

            color[node] = 0


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of colors: "))

print("Enter adjacency matrix:")
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

color = [0]*n

print("\nSolution:")
solve(0, graph, m, color)