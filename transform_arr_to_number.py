
def num(arr):
    res = reduce(lambda x, y: 10 * x + y, arr)
    return res

assert 123 == num([1, 2, 3])
assert 342 == num([3, 4, 2])
