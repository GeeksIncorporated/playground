visited = set()

M = [[0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0]]


def get_adjacencies(node):
    adjs = []
    x, y = node
    if x > 0:
        adjs.append((x - 1, y))
    if x < len(M) - 1:
        adjs.append((x + 1, y))
    if y > 0:
        adjs.append((x, y - 1))
    if y < len(M) - 1:
        adjs.append((x, y + 1))
    return adjs


def shortest_path(start, end):
    pathes = []
    if start == end:
        return 0

    visited.add(start)
    adjs = get_adjacencies(start)

    for adj in adjs:
        if adj in visited or M[adj[0]][adj[1]] == 1:
            continue
        pathes.append(shortest_path(adj, end))

    if not pathes:
        return 100

    print start, pathes
    return 1 + min(pathes)

print shortest_path((1, 0), (4, 4))
