# Breadth-first-search

from queue import Queue

def BFS(G, root, goal):
    q = Queue()
    visited = [root]
    q.put(root)
    while not q.empty():
        v = q.get()
        if v == goal:
            return v
        for child in G[v]:
            if not child in visited:
                visited.append(child)
                q.put(child)

# Graph definition
G = {
    'a' : ['b', 'c'],
    'b' : ['d', 'e'],
    'c' : ['f', 'g'],
    'd' : [],
    'e' : ['h'],
    'f' : [],
    'g' : [],
    'h' : []
}

print(BFS(G, 'a', 'f'))

