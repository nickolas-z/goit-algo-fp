import networkx as nx
import matplotlib.pyplot as plt
import heapq
from graph_data import create_graph


def dijkstra(graph, start)->tuple:
    """
    Пошук найкоротших шляхів від вказаної вершини до всіх інших вершин
    args:
        graph: Граф
        start: Початкова вершина
    returns:
        distances: Відстані до всіх вершин
        previous: Попередні вершини для кожної вершини
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Priority queue
    pq = [(0, start)]
    previous = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous

def get_path(previous, start, end)->list:
    """
    Відновлення шляху
    args:
        previous: Попередні вершини для кожної вершини
        start: Початкова вершина
        end: Кінцева вершина
    returns:
        list: Шлях
    """
    path = []
    current = end
    while current:
        path.append(current)
        if current == start:
            break
        current = previous[current]
    if path[-1] != start:
        # Немає шляху
        return None
    return path[::-1]

def draw_graph(G)->None:
    """
    Візуалізація графа
    args:
        G: Граф
    """
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=8, font_weight='bold')

    # Add edge labels with weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Зважений граф транспортної мережі Рівного", fontsize=16)
    plt.axis('off')
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.show()

if __name__ == "__main__":
    
    G = create_graph()

    # Пошук найкоротших шляхів між усіма парами вершин
    all_paths = {}
    for start in G.nodes:
        distances, previous = dijkstra(G, start)
        paths_from_start = {}
        for end in G.nodes:
            if start != end:
                path = get_path(previous, start, end)
                if path:
                    # print(f"Шлях від {start} до {end}: {' -> '.join(path)}")
                    paths_from_start[end] = (distances[end], path)
                else:
                    print(f"Шлях від {start} до {end} не існує")
        all_paths[start] = paths_from_start

    # Виведення найкоротших шляхів
    for start in G.nodes:
        print(f"\nНайкоротші шляхи від '{start}':")
        for end, (distance, path) in all_paths[start].items():
            print(f"  До '{end}': відстань = {distance:.1f} км, шлях = {' → '.join(path)}")

    draw_graph(G)