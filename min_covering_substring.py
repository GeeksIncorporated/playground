import sys
from collections import defaultdict

min_length = sys.maxint


def min_covering_subs(A, Q):
    global min_length
    result = None

    # set leftmost word index
    l = 0

    # this will store the counters of occurrence of q's inside A[l:r]
    H = defaultdict(int)
    for r in range(len(A)):

        # set counter in H if element A[r] is covered
        if A[r] in Q:
            H[A[r]] += 1

        # while Q is covered by A[l: r+1]
        while len(H) == len(Q):

            # store result if A[l: r+1] is shorter than seen before
            if min_length > r - l:
                min_length = r - l
                result = A[l:r+1]

            # if leftmost word is covered decrease it's counter
            if A[l] in Q:
                H[A[l]] -= 1

                # make the leftmost word uncovered if the counter is zero
                if H[A[l]] == 0:
                    del H[A[l]]

            # make next word to be the leftmost
            l += 1

    return result

a = "good we the champions so the we good are we the champions we are the".split(" ")
q = "we are the champions".split(" ")
print min_covering_subs(a, q)
