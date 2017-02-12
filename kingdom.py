from collections import defaultdict

class Node(defaultdict):

    def __init__(self, color):
        self.color = color
        super(Node, self).__init__()

def tree():
    return defaultdict(tree)

def one_of():
    yield "Red"
    yield "Blue"

kingdom = tree()
kingdom['1']['2']
kingdom['1']['3']
kingdom['3']['4']
kingdom['3']['5']


def dicts(t):
    return {k: dicts(t[k]) for k in t}


print dicts(kingdom)
