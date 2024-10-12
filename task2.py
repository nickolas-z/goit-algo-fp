import networkx as nx
import matplotlib.pyplot as plt
from graph_data import create_graph

def dfs_path(graph, start, end, path=None)->list:
    """ Search for a path from start to end using DFS """
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, end)->list:
    """ Search for a path from start to end using BFS """
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


if __name__ == "__main__":

    G = create_graph()

    # Start and end points
    start = "Залізничний вокзал"
    end = "Ювілейний"

    # Search for paths
    dfs_result = dfs_path(G, start, end)
    bfs_result = bfs_path(G, start, end)

    print(f"\nDFS шлях від '{start}' до '{end}':")
    print(" → ".join(dfs_result))

    print(f"\nBFS шлях від '{start}' до '{end}':")
    print(" → ".join(bfs_result))

    # Visualize the graph with DFS and BFS paths
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, k=0.5, iterations=50)

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=8, font_weight='bold')

    # Highlight the DFS path
    dfs_edges = list(zip(dfs_result, dfs_result[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='r', width=2)

    # Highlight the BFS path
    bfs_edges = list(zip(bfs_result, bfs_result[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='g', width=2)

    plt.title("Шляхи DFS (червоний) і BFS (зелений) у транспортній мережі м. Рівне", fontsize=16)
    plt.axis('off')

    # Adjust the plot to make room for the legend
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    # Add a legend
    red_line = plt.Line2D([], [], color="red", linewidth=2, label="DFS шлях")
    green_line = plt.Line2D([], [], color="green", linewidth=2, label="BFS шлях")
    plt.legend(handles=[red_line, green_line], loc="lower right")

    plt.show()

