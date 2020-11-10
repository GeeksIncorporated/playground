queen_pos = (4, 4)
obstacles = set([(2,3)])


def left(x, y):
    n = 0
    while x > 1:
        x -= 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def right(x, y):
    n = 0
    while x < n:
        x += 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def down(x, y):
    n = 0
    while y > 1:
        y -= 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def up(x, y):
    n = 0
    while y < n:
        y -= 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def left_down(x, y):
    n = 0
    while y > 1 and x > 1:
        y -= 1
        x -= 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def left_up(x, y):
    n = 0
    while y < n and x > 1:
        y += 1
        x -= 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def right_up(x, y):
    n = 0
    while y < n and x < n:
        y += 1
        x += 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


def right_down(x, y):
    n = 0
    while y > 1 and x < n:
        y -= 1
        x += 1
        if (x, y) in obstacles:
            break
        n += 1
    return n


print(left(4, 4))
print(right(4, 4))
print(up(4, 4))
print(down(4, 4))
print(left_down(4, 4))
print(left_up(4, 4))
print(right_up(4, 4))
print(right_down(4, 4))
