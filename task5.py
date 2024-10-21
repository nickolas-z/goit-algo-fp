import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from BinTree import add_edges
from task4 import build_heap_tree
from collections import deque
import copy


def draw_tree(tree_root, ax, traversal_type="") -> None:
    """ 
    Візуалізація бінарного дерева
    args:
        tree_root: корінь дерева
        ax: об'єкт візуалізації
        traversal_type: тип обходу (DFS або BFS)
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    # Показуємо значення вузла в мітках
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}  

    ax.clear()
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        ax=ax,
    )
    ax.set_title(f"Обхід бінарного дерева: {traversal_type}", fontsize=16)


def animate_traversal(tree_root, traversal_type="DFS")->None:
    """
    Анімація обходу бінарного дерева
    Args:
        tree_root: корінь дерева
        traversal_type: тип обходу (DFS або BFS)
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    frames = []

    if traversal_type == "DFS":
        stack = [tree_root]
        visited = set()

        while stack:
            node = stack.pop()
            if node:
                # Створюємо копію дерева, щоб змінювати лише колір вузлів у копії (оригінал залишається незмінним)
                tree_copy = copy.deepcopy(tree_root)
                node_copy = find_node_by_id(tree_copy, node.id)
                if node_copy:
                    # Жовтий колір для поточного вузла
                    node_copy.color = "#FFFF00"
                for visited_node in visited:
                    visited_node_copy = find_node_by_id(tree_copy, visited_node.id)
                    if visited_node_copy:
                        # Відвідані вузли зображаємо темно-синім кольором
                        visited_node_copy.color = "#1296F0"
                frames.append(tree_copy)
                visited.add(node)
                stack.append(node.right)
                stack.append(node.left)

    elif traversal_type == "BFS":
        queue = deque([tree_root])
        visited = set()

        while queue:
            node = queue.popleft()
            if node:
                # Створюємо копію дерева, щоб змінювати лише колір вузлів у копії, а не в оригіналі
                tree_copy = copy.deepcopy(tree_root)
                node_copy = find_node_by_id(tree_copy, node.id)
                if node_copy:
                    # Поточний вузол відображається жовтим
                    node_copy.color = "#FFFF00"
                for visited_node in visited:
                    visited_node_copy = find_node_by_id(tree_copy, visited_node.id)
                    if visited_node_copy:
                        # Відвідані вузли зображаємо темно-синім кольором
                        visited_node_copy.color = "#1296F0"
                frames.append(tree_copy)
                visited.add(node)
                queue.append(node.left)
                queue.append(node.right)

    def update(frame, traversal_type):
        draw_tree(frame, ax, traversal_type)

    ani = animation.FuncAnimation(
        fig, update, frames=frames, repeat=False, interval=500, fargs=(traversal_type,)
    )
    # Зберігаємо анімацію у файл
    # ani.save(f"{traversal_type}_traversal.mp4", writer="ffmpeg")
    ani.save(f"{traversal_type}_traversal.gif", writer="imagemagick")
    plt.show()


def find_node_by_id(tree_root, node_id)->None:
    """ 
    Пошук вузла за його ідентифікатором у дереві
    args:
        tree_root: корінь дерева
        node_id: ідентифікатор вузла
    """
    if tree_root is None:
        return None
    if tree_root.id == node_id:
        return tree_root
    left_result = find_node_by_id(tree_root.left, node_id)
    if left_result:
        return left_result
    return find_node_by_id(tree_root.right, node_id)


def main():
    """ Основна функція """
    # Задання для бінарної купи
    heap_array = [10, 5, 3, 2, 4, 1, 7, 6, 8, 9, 11, 12, 13, 14, 15]

    # Створення дерева із купи
    heap_tree_root = build_heap_tree(heap_array)

    # Візуалізація обходу в глибину
    if heap_tree_root:
        print("Запуск DFS візуалізації")
        animate_traversal(heap_tree_root, traversal_type="DFS")

    # Візуалізація обходу в ширину
    if heap_tree_root:
        print("Запуск BFS візуалізації")
        animate_traversal(heap_tree_root, traversal_type="BFS")    

if __name__ == "__main__":
    main()
