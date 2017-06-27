from collections import defaultdict


def f5():
    import random  # for f5 use only
    return random.randint(1, 5)


def f7():
    """
    We can use the pairs (a,b) where a <- f5() and b<-f5
    It's clear that there are 25 such pairs where each one 
    is repeated only once.
    We can map: 
    (1,1) --> 1
    (1,2) --> 2
    ..
    (2,1) --> 6
    (2,2) --> 7
    We also can call f5() till we get a and b so that (a,b) 
    belongs to the mapping. The probability to get such a pair is equal 
    for each pair and equals to 1/25. So the requirement for equal 
    distribution is fulfilled.
    :return: 
    """

    mapping = {(1, 1): 1,
               (1, 2): 2,
               (1, 3): 3,
               (1, 4): 4,
               (1, 5): 5,
               (2, 1): 6,
               (2, 2): 7}

    # Loop till the needed pair is encountered
    while True:
        a = f5()
        b = f5()
        if (a, b) in mapping:
            return mapping[(a, b)]


# Counting and printing the distribution to
# visually confirm the almost-equality
counters = defaultdict(int)
for i in xrange(10000):
    r = f7()
    counters[r] += 1

print counters