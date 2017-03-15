

def Hanoi(h, A, B, C):
    if h > 0:
        Hanoi(h - 1, A, C, B)
        print "Moving disk from %s to %s" % (A, C)
        Hanoi(h - 1, B, A, C)


Hanoi(3, "A", "B", "C")
