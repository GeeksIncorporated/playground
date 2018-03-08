import random


def msort(A):
    if len(A) == 1:
        return A

    m = int(len(A) / 2)
    l = msort(A[:m])
    r = msort(A[m:])
    i = j = 0
    results = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            results.append(l[i])
            i += 1
        else:
            results.append(r[j])
            j += 1

    results += l[i:]
    results += r[j:]
    return results


print msort([random.randint(1, 100) for x in range(100)])
