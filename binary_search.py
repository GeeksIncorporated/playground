import random


def bs1(arr, x):
    l = 0
    r = len(arr)

    while l < r:
        mid = l + (r - l) / 2
        if x < arr[mid]:
            r = mid
        elif x > arr[mid]:
            l = mid
        else:
            return mid

    return None

arr = range(100)
for i in range(100):
    x = random.randint(1, 99)
    r1 = bs1(arr, x)
    print x, r1
    assert r1 == x
