import matplotlib.pyplot as plt
import networkx as nx
from names import nodes
from relation import relationships
from color_map import color_map

# Create a graph
G = nx.Graph()

# Add nodes with attributes
for person, attr in nodes.items():
    G.add_node(person, **attr)

# Add edges with relationship types
for person, friends in relationships.items():
    for friend, relation in friends.items():
        G.add_edge(person, friend, relation=relation)


# Define the search person
search_person = input("Enter the name of he person to search for : ")


if  search_person in nodes :
    # Create a subgraph with the search person and their direct connections
    subgraph_nodes = set(G.neighbors(search_person)) | {search_person}
    subgraph = G.subgraph(subgraph_nodes)

    # Define node colors based on relationships
    node_colors = {}
    for node in subgraph.nodes():
        # Find the most significant relationship (or any other logic you prefer)
        relationships = [G[u][v]['relation'] for u, v in G.edges(node) if 'relation' in G[u][v]]
        if relationships:
            # Use the color of the most frequent relation
            most_frequent_relation = max(set(relationships), key=relationships.count)
            node_colors[node] = color_map.get(most_frequent_relation, 'lightblue')
        else:
            # Default color if no relations
            node_colors[node] = 'lightblue'

    # Use a spring layout and center the search person
    pos = nx.spring_layout(subgraph, seed=42)
    pos[search_person] = [0, 0]  # Place the search person at the center

    # Draw the subgraph
    plt.figure(figsize=(12, 10))

    # Draw nodes with assigned colors
    nx.draw_networkx_nodes(subgraph, pos, node_color=[node_colors[node] for node in subgraph.nodes()], node_size=500, edgecolors='black')

    # Draw edges with default color
    nx.draw_networkx_edges(subgraph, pos, edge_color='black', alpha=0.7)

    # Draw labels with age information
    nx.draw_networkx_labels(subgraph, pos, labels={node: f"{node}\n({subgraph.nodes[node]['age']} years)" for node in subgraph.nodes()})

    # Highlight the search person's node
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[search_person], node_color='lightgreen', node_size=800, edgecolors='black')

    plt.title(f'Network of {search_person} and Their Connections')
    plt.show()
else:
    print("Not Found in the database !")