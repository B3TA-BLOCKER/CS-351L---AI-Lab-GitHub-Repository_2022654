# A* is an informed search Algorithm which means it will take into account the location of the goal while deciding the next move  
# Basically ther is a cost associated to with each cell of the maze an A* will try to select the path with minimum cost 
# f(n) = g(n) + h(n)

# f(n) is the cost of the node or the cell and it has two components "g(n) and h(n)"

# g(n) --> is the cost of the path from start node to n.
# h(n) --> is a heuristic function that estimates the cost of the cheapest path from n to the goal 

from pymaze import maze
