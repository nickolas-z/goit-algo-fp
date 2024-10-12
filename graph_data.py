import networkx as nx

def create_graph():
    # Create a graph for the transport network of Rivne
    G = nx.Graph()
    stops = [
        "Залізничний вокзал", "Центр", "Автовокзал", "Пивзавод", 
        "12 школа", "Мототрек", "Льонокомбінат", "Боярка", 
        "Північний", "Ювілейний"
    ]
    G.add_nodes_from(stops)

    weighted_routes = [
        ("Залізничний вокзал", "Центр", 2.5),
        ("Центр", "Автовокзал", 1.8),
        ("Автовокзал", "Пивзавод", 3.2),
        ("Пивзавод", "12 школа", 2.1),
        ("12 школа", "Мототрек", 2.7),
        ("Мототрек", "Льонокомбінат", 3.5),
        ("Льонокомбінат", "Боярка", 2.9),
        ("Боярка", "Північний", 1.6),
        ("Північний", "Ювілейний", 2.3),
        ("Ювілейний", "Центр", 3.8),
        ("Центр", "Пивзавод", 2.6),
        ("Автовокзал", "Мототрек", 4.1),
        ("12 школа", "Боярка", 3.3),
    ]
    G.add_weighted_edges_from(weighted_routes)

    return G

if __name__ == "__main__":
    G = create_graph()
    print("\nNodes of the graph:")
    print(G.nodes(data=True))

    print("\nEdges of the graph:")
    print(G.edges(data=True))



