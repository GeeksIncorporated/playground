from collections import defaultdict

G = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['A', 'C', 'B']
}

RED = 0
BLUE = 1
GREEN = 2

NODES = defaultdict(lambda: {"color": None})
solutions = []


def is_safe(node, color):
    for child in G[node]:
        if NODES[child]["color"] == color:
            return False
    return True

nodes = list(G.keys())

def paint_graph():
    if len(nodes) == 0:
        print(NODES)
    else:
        node = nodes.pop()
        for color in (RED, BLUE, GREEN):
            if is_safe(node, color):
                NODES[node]["color"] = color
                paint_graph()

paint_graph()
