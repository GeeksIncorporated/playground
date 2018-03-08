import time
import random
from copy import copy

n = 1000
arr = [random.randint(0, n) for i in range(n)]


def is_sorted(arr):
    last = arr[0]
    for a in arr:
        if a < last:
            return False
        last = a
    return True


def shuffle(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = random.randint(l, r)
        if arr[l] <= arr[m]:
            l += 1
            continue
        arr[m], arr[l] = arr[l], arr[m]
        l += 1
    return arr

def stupid_sort(arr):
    while True:
        shuffle(arr)
        print(arr)
        if is_sorted(arr):
            return arr


st = time.time()
print(stupid_sort(copy(arr)))
print(time.time() - st)
