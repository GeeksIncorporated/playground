import random


def bs1(arr, x):
    l = 0
    r = len(arr)

    while True:
        i = (r - l) / 2 + l
        if x < i:
            r = i
        elif x > i:
            l = i
        else:
            return i
        print l, r
        if r - l == 1:
            return None


def bs2(arr, x):
    i = len(arr) / 2

    if not arr:
        return None

    if arr[i] == x:
        return i

    if x < arr[i]:
        return bs2(arr[:i], x)
    elif x > arr[i]:
        return bs2(arr[i + 1:], x)


arr = range(100)
for i in range(100):
    x = random.randint(1, 200)
    r1 = bs1(arr, x)
    r2 = bs2(arr, x)
    assert r1 == r2
