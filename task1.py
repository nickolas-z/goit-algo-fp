import networkx as nx
import matplotlib.pyplot as plt
from graph_data import create_graph

def describe_graph(G)->None:
    """ Describe the graph """
    
    # Basic analysis
    print(f"Кількість вершин (зупинок): {G.number_of_nodes()}")
    print(f"Кількість ребер (маршрутів): {G.number_of_edges()}")
    print("\nСтупінь вершин (кількість з'єднань для кожної зупинки):")
    for node, degree in G.degree():
        print(f"'{node}': {degree}")
    
    # Advanced analysis
    print(f"\nЩільність графа: {nx.density(G):.4f}")
    print(f"Діаметр графа: {nx.diameter(G)}")
    print(f"Середній найкоротший шлях: {nx.average_shortest_path_length(G):.4f}")

def draw_graph(G)->None:
    """ Visualize the graph """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=8, font_weight='bold')
    edge_labels = {(u, v): '' for (u, v) in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Спрощена модель транспортної мережі м. Рівне")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    G = create_graph()
    describe_graph(G)
    draw_graph(G)