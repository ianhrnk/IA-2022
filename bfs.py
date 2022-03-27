# Breadth-first-search

from queue import Queue


def BFS(G, root, goal):
    queue = Queue()
    visited = [root]
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        if node == goal:
            return node
        for child in G[node]:
            if not child in visited:
                visited.append(child)
                queue.put(child)


# Graph definition
G = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": [],
    "e": ["h"],
    "f": [],
    "g": [],
    "h": [],
}

print(BFS(G, "a", "f"))
