import random
from copy import copy
import time

n = 10
arr = [random.randint(0, n) for i in range(n)]
c = 0

def checksorted(arr):
    last = -1
    for i, a in enumerate(arr):
        if a < last:
            return False
        last = a
    return True


def stupid_sort(arr):
    while True:
        if c % 1000 == 0:
            print(arr)
        random.shuffle(arr)
        if checksorted(arr):
            return arr


st = time.time()
res = stupid_sort(copy(arr))
print(time.time() - st)
print(res)
