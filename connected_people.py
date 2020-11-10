"""
Given that all family members knows each other,
as well as all people that living in the same town, knows each other. 
Find the minimal connections between 2 diffrent people, 
to get them "know" each other.
"""

from queue import Queue
from collections import defaultdict
from pprint import pprint

persons = (("Vishnevsky", "Haifa"),
           ("Vishnevsky", "Toronto"),
           ("Bagrov", "Kharkov"),
           ("Bagrov", "Haifa"),
           ("Danilov", "Tbilisi"),
           ("Danilov", "Haifa"),
           ("Soloduha", "Rio De Janeiro"),
           ("Soloduha", "Migdal"),
           ("Ivanov", "Migdal"),
           ("Ivanov", "Kutaisi"),
           ("Petrov", "Kharkov"),
           ("Petrov", "Kiev"),
           ("Petrov", "Toronto"),
           ("Petrov", "Rio De Janeiro"))

names2cities = defaultdict(set)
cities2names = defaultdict(set)

for name, city in persons:
    names2cities[name].add(city)
    cities2names[city].add(name)


def get_all_direct_connections(person):
    p_name, p_city = person
    connected_people = set()
    for city in names2cities[p_name]:
        connected_people.add((p_name, city))
    for name in cities2names[p_city]:
        connected_people.add((name, p_city))
    connected_people.remove(person)
    return connected_people


def solve(person1, person2):
    visited = set()
    parent = {person1: None}

    def bfs(person1, person2):

        # Trivial Case
        if person1 == person2:
            return 0

		# BFS with loop and Queue
		# we weill be storing (# #) in queue as a delimiter
		# to indicate the tree-level is done so the depth counter
		# should be increased.
        q = Queue()
        q.put(person1)
        q.put(("#", "#"))
        depth = 1

        while q.qsize() > 1:
            person = q.get()

			# delimeter is met, the depth increases
            if person == ("#", "#"):
                depth += 1
                q.put(person)	# delimeter reenqueued
                continue

            visited.add(person)

            for direct_connection in get_all_direct_connections(person):
                if direct_connection in visited:
                    continue
				# store the parent for this connection
				# we will use it to restore the whole path
                parent[direct_connection] = person

				# found the target person
                if direct_connection == person2:
                    return depth

				# enque connection for further search
                q.put(direct_connection)

		# the target person was not found
        return -1

    res = bfs(person1, person2)

	# Restoring the whole path
    p = person2
    connection = []
    for i in range(res + 1):
        connection.append(p)
        p = parent[p]
    print("%s connections between %s and %s:" % (res, person1, person2))
    pprint(list(reversed(connection)))


solve(("Vishnevsky", "Haifa"),
      ("Petrov", "Kiev"))

solve(("Vishnevsky", "Haifa"),
      ("Soloduha", "Migdal"))

solve(("Vishnevsky", "Haifa"),
      ("Vishnevsky", "Haifa"))

# 3 connections between ('Vishnevsky', 'Haifa') and ('Petrov', 'Kiev'):
# [('Vishnevsky', 'Haifa'),
#  ('Vishnevsky', 'Toronto'),
#  ('Petrov', 'Toronto'),
#  ('Petrov', 'Kiev')]
# 5 connections between ('Vishnevsky', 'Haifa') and ('Soloduha', 'Migdal'):
# [('Bagrov', 'Haifa'),
#  ('Bagrov', 'Kharkov'),
#  ('Petrov', 'Kharkov'),
#  ('Petrov', 'Rio De Janeiro'),
#  ('Soloduha', 'Rio De Janeiro'),
#  ('Soloduha', 'Migdal')]
# 0 connections between ('Vishnevsky', 'Haifa') and ('Vishnevsky', 'Haifa'):
# [('Vishnevsky', 'Haifa')]