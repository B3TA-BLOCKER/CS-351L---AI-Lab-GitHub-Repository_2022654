# A* is an informed search Algorithm which means it will take into account the location of the goal while deciding the next move  
# Basically ther is a cost associated to with each cell of the maze an A* will try to select the path with minimum cost 
# f(n) = g(n) + h(n)

# f(n) is the cost of the node or the cell and it has two components "g(n) and h(n)"

# g(n) --> is the cost of the path from start node to n.
# h(n) --> is a heuristic function that estimates the cost of the cheapest path from n to the goal 


# A* Algorithm

def a_star_algo(start, target):
    open_set = set([start])
    close_set = set()
    g = {}  # store distance from the starting node
    parents = {}  # parent contains an adjacency map of all nodes

    # distance from the starting node to itself is zero
    g[start] = 0

    # start node is the root node it has no parent nodes
    # so start node is set as its parent node
    parents[start] = start

    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for i in open_set:
            if n is None or g[i] + heuristic(i) < g[n] + heuristic(n):
                n = i

        if n is None:
            print("Path does not exist !!")
            return None


        # if the current node is the target
        # then we begin reconstructing the path from it to the start node
        if n == target:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start)
            path.reverse()

            print("Path Found {}".format(path))
            return path


        # remove n from the open list and add it to the closed list
        open_set.remove(n)
        close_set.add(n)


        # explore neighbors
        for (m, weight) in get_neighbors(n):
            if m in close_set:
                continue

            tentative_g = g[n] + weight

            if m not in open_set:
                open_set.add(m)
            elif tentative_g >= g.get(m, float('inf')):
                continue

            g[m] = tentative_g
            parents[m] = n

    print("Path does not exist !!")
    return None


# Function to return neighbor and its distance from the given node

def get_neighbors(node):
    if node in Graph_nodes:
        return Graph_nodes[node]
    return []


# Heuristic function

def heuristic(node):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return H_dist[node]



# Graph nodes
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

a_star_algo('A', 'G')
