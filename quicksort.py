import time
import random


def shuffle(arr, l, r):
    m = l
    p = random.randint(l, r)
    arr[p], arr[r] = arr[r], arr[p]

    while l < r:
        if arr[l] < arr[r]:
            arr[l], arr[m] = arr[m], arr[l]
            m += 1
        l += 1

    arr[m], arr[r] = arr[r], arr[m]
    return m


def stupid_sort(arr, l, r):
    if l >= r:
        return
    p = shuffle(arr, l, r)
    stupid_sort(arr, l, p)
    stupid_sort(arr, p + 1, r)


n = 100000
arr = [random.randint(1, n) for i in range(n)]
st = time.time()
stupid_sort(arr, 0, len(arr) - 1)
print(time.time() - st)
print(arr)
