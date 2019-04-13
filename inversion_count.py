counter = 0

def inv_count(A):
    global counter
    if len(A) == 1:
        return A

    mid = len(A) / 2
    l = inv_count(A[:mid])
    r = inv_count(A[mid:])
    i = j = 0
    results = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            results.append(l[i])
            i += 1
        else:
            counter += len(l) - i
            results.append(r[j])
            j += 1

    results += l[i:]
    results += r[j:]
    return results

print(inv_count([3,2,4,1,0]))
print(counter)