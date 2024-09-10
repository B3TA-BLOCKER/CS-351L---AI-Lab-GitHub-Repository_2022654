from collections import deque

# BFS from given source s
def bfs(adj, s, visited):
  
    # Create a queue for BFS
    q = deque()

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
      
        # Dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        # Get all adjacent vertices of the dequeued 
        # vertex. If an adjacent has not been visited, 
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)



# Number of vertices in the graph
V = 5

# Adjacency list representation of the graph
adj = [[] for _ in range(V)]

# Add edges to the graph
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 1, 4)
add_edge(adj, 2, 4)

# Mark all the vertices as not visited
visited = [False] * V

# Perform BFS traversal starting from vertex 0
print("BFS starting from 0: ")
bfs(adj, 0, visited)
