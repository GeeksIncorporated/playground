"""
Given 2d field where 0 denotes empty cell and 1 denotes filled with oil,
count the size of the largest oil field. The oil field formed 
by adjacent cells connected horizontally or vertically:

0 0 1 1 1
1 0 1 0 1
1 0 1 1 1
1 0 0 0 0

Answer: 8
"""

M = [[0, 1, 1, 1, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 1],
     [0, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 1, 0, 0],
     [1, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0, 0, 1, 0],
     [1, 0, 1, 0, 1, 1, 0, 0]]


# Yields the next node, belonging to the oil field.
def get_adjs(node):
    x, y = node
    l = len(M) - 1

    # Check nodes adjacent neighbours
    for i, j in ((max(0, x - 1), y),  # look left
                 (min(l, x + 1), y),  # look right
                 (x, min(l, y + 1)),  # look up
                 (x, max(0, y - 1))):  # look down

        # if there is oil, yield it
        if M[i][j]:
            yield i, j


# DFS runs on oil field and count it's size
def dfs(node):

    q = []
    q.append(node)
    counter = 0
    while q:
        node = q.pop()
        visited.add(node)
        counter += 1
        for adj in get_adjs(node):
            if adj not in visited:
                q.append(adj)
    return counter


visited = set()
field_size = 0

for i in xrange(len(M)):
    for j in xrange(len(M)):

        if M[i][j] == 0:  # No oil
            continue

        if (i, j) in visited:  # Already been there
            continue

        field_size = max(field_size, dfs((i, j)))

print field_size

