from copy import copy
from collections import defaultdict

def create_graph(pairs) :
    G = defaultdict(set) 
    if not pairs:
        return G
    for pair in pairs :
        a,b = pair
        G[a].add(b)
        G[b].add(a)
    return G

def find_largest_connected_group(pairs):
    connected_groups = []
    visited = set()
    
    def dfs(item, group) :
        group.append(item)
        visited.add(item) 
        adjacent_items = G.get(item)
        
        # if item has no adjacents 
        # but the parent
        if len(adjacent_items) == 1:
            connected_groups.append(
            	    copy(group))
            group=[]
            return
        
        # continue with dfs
        for item in adjacent_items:
            if item not in visited:
                dfs(item, group) 
                
    G = create_graph(pairs) 
    
    if not G:
        return []
    
    # populates connected_groups
    # by starting dfs for each 
    # unvisited item
    for item in G.keys():
        if item not in visited:
            dfs(item,[])
    
    # find Max connected_group
    max_items = 0
    max_group = []
    for g in connected_groups:
        if max_items < len(g) :
            max_items = len(g) 
            max_group = g
    return max_group

print find_largest_connected_group(
    [[1,2],[1,3],[2,4],[3,5],[6,7]]
)