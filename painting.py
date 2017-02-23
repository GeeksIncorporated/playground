import pprint

arr1 = [[1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]]


def get_neighbors(arr, x, y):
    points = set()
    for i in range(max(x - 1, 0), min(x + 2, len(arr))):
        for j in range(max(y - 1, 0), min(y + 2, len(arr))):
            points.add(tuple([i, j]))
    points.discard(tuple([x, y]))
    return points


counter = 0


def recolor(arr, x, y):
    global counter
    counter += 1
    arr[x][y] = int(not arr[x][y])
    neighbors = get_neighbors(arr, x, y)
    for point in neighbors:
        if arr[point[0]][point[1]] != arr[x][y]:
            recolor(arr, point[0], point[1])


pprint.pprint(arr1)
recolor(arr1, 8, 0)
print
pprint.pprint(arr1)
print counter
