import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math


class Node:
    def __init__(self, key, color="skyblue"):
        """ Конструктор класу Node """
        self.left = None
        self.right = None
        self.val = key
        # Додатковий аргумент для зберігання кольору вузла
        self.color = color
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1)->nx.DiGraph:
    """ 
    Функція для додавання вузлів та ребер у граф 
    та визначення позицій вузлів для візуалізації 
    Args:
        graph: Об'єкт графа
        node: Поточний вузол
        pos: Словник позицій вузлів
        x: Координата x
        y: Координата y
        layer: Рівень вузла
    return: Об'єкт графа
    """
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та зберігання значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root)->None:
    """ 
    Функція для візуалізації бінарного дерева 
    Args:
        tree_root: Корінь дерева
    return: None
    """   
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(arr, index=0):
    """Функція для побудови бінарного дерева з масиву"""
    # Базовий випадок: якщо індекс за межами масиву
    if index >= len(arr):
        return None

    # Створюємо вузол для кожного елемента масиву
    node = Node(arr[index])

    # Рекурсивно додаємо лівий та правий вузоли
    node.left = build_heap_tree(arr, 2 * index + 1)
    node.right = build_heap_tree(arr, 2 * index + 2)

    return node


def main()->None:
    """ Основна функція """
    # Задання для бінарної купи
    heap_array = [10, 5, 3, 2, 4, 1]

    # Створення дерева із купи
    heap_tree_root = build_heap_tree(heap_array)

    # Візуалізація дерева
    if heap_tree_root:
        draw_tree(heap_tree_root)

if __name__ == "__main__":
    main()
