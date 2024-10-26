from BinTree import Node, draw_tree


def build_heap_tree(arr, index=0) -> Node:
    """
    Функція для побудови бінарного дерева з масиву
    args:
        arr: масив
        index: індекс поточного елемента
    returns:
        node: вузол
    """
    # Базовий випадок: якщо індекс за межами масиву
    if index >= len(arr):
        return None

    # Створюємо вузол для кожного елемента масиву
    node = Node(arr[index])

    # Рекурсивно додаємо лівий та правий вузоли
    node.left = build_heap_tree(arr, 2 * index + 1)
    node.right = build_heap_tree(arr, 2 * index + 2)

    return node


def main() -> None:
    """Основна функція"""
    # Задання для бінарної купи
    heap_array = [10, 5, 3, 2, 4, 1, 7, 6, 8, 9, 11, 12, 13, 14, 15]

    # Створення дерева із купи
    heap_tree_root = build_heap_tree(heap_array)

    # Візуалізація дерева
    if heap_tree_root:
        draw_tree(heap_tree_root, "Візуалізація піраміди")


if __name__ == "__main__":
    main()
