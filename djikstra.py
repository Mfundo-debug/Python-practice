"""
Using Djikstra algorithm to search for the shortest path between two points in a graph
In a graph, the shortest path between two points is the path with the minimum weight

"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def djikstra_algorithm(graph, start, end):
    """
    Find the shortest path between two points in a graph using Djikstra's algorithm.
    """
    # Initialize the shortest path
    shortest_path = []
    # Initialize the queue
    queue = []
    # Add the start node to the queue
    queue.append([start])
    # Loop until the queue is empty
    while queue:
        # Get the first path from the queue
        path = queue.pop(0)
        # Get the last node from the path
        node = path[-1]
        # Check if the node is the end node
        if node == end:
            # Update the shortest path
            shortest_path = path
            break
        # Loop through the neighbors of the node
        for neighbor in graph[node]:
            # Check if the neighbor has not been visited
            if neighbor not in path:
                # Create a new path
                new_path = list(path)
                new_path.append(neighbor)
                # Add the new path to the queue
                queue.append(new_path)
    return shortest_path

if __name__ == '__main__':
    # Create a graph
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 3},
        'C': {'A': 4, 'F': 5},
        'D': {'B': 2},
        'E': {'B': 3, 'F': 1},
        'F': {'C': 5, 'E': 1}
    }
    # Create a networkx graph
    G = nx.Graph(graph)
    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()
    # Find the shortest path between two points
    start = 'A'
    end = 'F'
    shortest_path = djikstra_algorithm(graph, start, end)
    print(shortest_path)