import time
import random


def is_sorted(arr):
    last = arr[0]
    for a in arr:
        if a < last:
            return False
        last = a
    return True


def shuffle(arr, l, r):
    rint = random.randint
    while l < r:
        m = rint(l, r)
        if arr[l] > arr[m]:
            arr[m], arr[l] = arr[l], arr[m]
        l += 1
    return arr


def stupid_sort(arr):
    while True:
        shuffle(arr, 0, len(arr) - 1)
        if is_sorted(arr):
            return arr


n = 100
arr = [random.randint(0, n) for i in range(n)]

st = time.time()
print((stupid_sort(arr)))
print((time.time() - st))
