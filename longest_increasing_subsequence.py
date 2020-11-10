import bisect

a = [28, 33, 95, 63, 33, 35, 83, 29, 84, 99]


def find_lis(arr):
    M = []
    for i in range(len(arr)):
        el = arr[i]
        ind = bisect.bisect_right(M, el)
        if ind < len(M):
            M[ind] = el
        else:
            M.append(el)
    return M


lis = find_lis(a)
print(lis)
print((len(lis)))
