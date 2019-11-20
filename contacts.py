# https://www.hackerrank.com/challenges/contacts/problem
# We're going to make our own Contacts application! The application must perform two types of operations:
#
#     add name, where
#
# is a string denoting a contact name. This must store
# as a new contact in the application.
# find partial, where
# is a string denoting a partial name to search the application for. It must count the number of contacts starting with
#
#     and print the count on a new line.
#
# Given
# sequential add and find operations, perform each operation in order.

# !/bin/python3

import os
import sys


#
# Complete the contacts function below.
#
def contacts(queries):
    pf = PreffixTree()
    output = []
    for query in queries:
        command, name = query
        if command == "add":
            pf.add(name)
        if command == "find":
            output.append(pf.find(name))
    return output


class PreffixTree:
    def __init__(self):
        self.root = {"count": 0}

    def add(self, name):
        current = self.root
        for c in name:
            current["count"] += 1
            if c not in current:
                current[c] = {"count": 0}
            current = current[c]

    def find(self, name):
        current = self.root
        for c in name:
            if c not in current:
                return 0
            current = current[c]
        return current['count'] + 1


if __name__ == '__main__':

    queries_str = [
        "add s"
        "add ss",
        "find s",
        "find ss"]

    queries = []
    for q in queries_str:
        queries.append(q.split(' '))
    print(queries)
    result = contacts(queries)
    print(result)
    assert result == [5, 4, 3, 2, 1, 0]
