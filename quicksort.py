"""
Classic inplace quicksort implementation taken from 
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-4-quicksort-randomized-algorithms/
"""

import random


def sort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        sort(A, l, p)
        sort(A, p + 1, r)
    return A


def partition(A, p, r):
    i = p
    for j in xrange(p + 1, r):
        if A[j] <= A[p]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i], A[p] = A[p], A[i]
    return i


A = [random.randint(1, 10) for i in xrange(20)]
print A
print sort(A, 0, len(A))
