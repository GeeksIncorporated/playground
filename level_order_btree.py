"""
https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true

You are given a pointer to the root of a binary tree.
You need to print the level order traversal of this tree.
In level order traversal, we visit the nodes level by level from left to right

Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


from queue import Queue


def levelOrder(root):
    q = Queue()
    q.put(root)
    q.put("#")
    res = []
    while not q.empty():
        node = q.get()
        if node == "#":
            continue
        else:
            res.append(str(node.info))
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
        if node.left or node.right:
            q.put("#")
    return res


tree = BinarySearchTree()

arr = [1, 2, 5, 3, 6, 4]

for a in arr:
    tree.create(a)

assert levelOrder(tree.root) == list(map(str, arr))
print(levelOrder(tree.root))