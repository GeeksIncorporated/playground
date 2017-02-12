from copy import copy, deepcopy


class Peg:
    def __init__(self, name):
        self.disks = []
        self.name = name

    def empty(self):
        return len(self.disks) == 0

    def __repr__(self):
        return str(self.disks)


def Hanoi(h, A, B, C):

    if h > 0:
        Hanoi(h - 1, A, C, B)
        print "Moving disk from %s to %s" % (A, C)
        Hanoi(h - 1, B, A, C)


Hanoi(30, "A", "B", "C")
