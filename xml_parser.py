import re
from copy import deepcopy

xml = """<root>
<a>aaa</a>
<sub>
<b>yyy</b>
</sub>
</root>
"""

class Node:
    def __init__(self, node_type, node_name):
        self.node_name = node_name
        self.node_type = node_type
        self.children = {}

    def __repr__(self):
        return "Node: %s %s" % (self.node_name, self.node_type)


def stream(xml):
    for node_name in re.findall("<.*?>|\w+", xml):
        if node_name.startswith("</"):
            node_type = "end"
        elif node_name.startswith("<"):
            node_type = "start"
        else:
            node_type = "data"
        yield Node(node_type, node_name)


def xml2json(xml):
    nodes = stream(xml)
    stack = []
    depth = -1
    node = next(nodes)
    stack.append(node)
    result = {}
    while len(stack) > 0:
        node = stack.pop()
        if node.node_type != "end":
            if node.node_type == "start":
                data = []
                depth += 1
            stack.append(node)
            stack.append(next(nodes))
        else:
            depth -= 1
            while node.node_type != "start":
                node = stack.pop()
                if node.node_type == "data":
                    data.append(node.node_name)
                else:
                    depth -= 1

            if data:
                data_field = (node.node_name, data)
            else:
                parent = dict()
                parent[node.node_name] = deepcopy(result)
                result = parent
    return result


print(xml2json(xml))
