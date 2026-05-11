from queue import PriorityQueue

goal = [[1,2,3],[4,5,6],[7,8,0]]

def h(state):
    c = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                c += 1
    return c

start = []

print("Enter puzzle:")

for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

pq = PriorityQueue()
pq.put((h(start), start))

print("Initial State:")
for row in start:
    print(row)

print("Heuristic Value =", h(start))