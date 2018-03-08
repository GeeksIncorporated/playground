import sys
import time
import random
from copy import copy

n = 1000
arr = [random.randint(0, n) for i in xrange(n)]
print arr


def checksorted(arr):
    last = arr[0]
    for a in arr:
        if a < last:
            return False
        last = a
    return True


def shuffle(arr):
    l = 0
    r = len(arr) - 1
    rint = random.randint
    while l < r:
        m = rint(l, r)
        if arr[l] < arr[m]:
            continue
        arr[l], arr[m] = arr[m], arr[l]
        l += 1

c = 0


def stusort1(arr):
    while True:
        shuffle(arr)
        if checksorted(arr):
            print arr
            break


st = time.time()
stusort1(copy(arr))
print(time.time() - st)


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


print(arr)
st = time.time()
bubbleSort(arr)
print(time.time() - st)
print(arr)
