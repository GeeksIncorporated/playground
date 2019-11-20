
def find_pair(a, s):
    l = 0
    r = len(a) - 1
    while l < r:
        c = a[l] + a[r]
        if c < s:
            l += 1
        elif c > s:
            r -= 1
        else:
            return a[l], a[r]
    return -1

assert find_pair([1, 1, 3, 3, 5], 6) == (1, 5)
assert find_pair([1, 1, 3, 3, 5], 4) == (1, 3)
assert find_pair([1, 1, 3, 3, 5], 3) == -1
assert find_pair([1, 1, 3, 5, 5], 2) == (1, 1)
