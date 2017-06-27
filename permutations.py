
def perms(A) :

    if len(A) == 2:
        yield A
        yield [A[1],A[0]]
        
    for i in xrange(len(A)) :
        for p in perms(A[:i] + A[i+1:]):
            yield [A[i]] + p

for i in perms(range(3)):
    print i