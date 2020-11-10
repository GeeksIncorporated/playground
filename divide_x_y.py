PRECISION = 0.0000000000001


def divide_x_y(x, y):
    l = 0
    r = x
    while l < r:

        k = l + float(r - l) * 0.5

        candidate = k * y

        if x - PRECISION < candidate < x + PRECISION:
            return k

        elif candidate < x:
            l = k

        elif candidate > x:
            r = k


print(divide_x_y(10, 3))
